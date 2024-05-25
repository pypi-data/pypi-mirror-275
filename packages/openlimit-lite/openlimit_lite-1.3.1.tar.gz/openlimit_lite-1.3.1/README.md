# openlimit-lite

Forked from https://github.com/shobrook/openlimit. Maintaining for our own use, stripping down to remove Redis dependencies.

A simple tool for maximizing usage of the OpenAI API without hitting the rate limit.

- Handles both _request_ and _token_ limits
- Precisely (to the millisecond) enforces rate limits with one line of code
- Handles _synchronous_ and _asynchronous_ requests

Implements the [generic cell rate algorithm,](https://en.wikipedia.org/wiki/Generic_cell_rate_algorithm) a variant of the leaky bucket pattern.

## Usage

### Define a rate limit

First, define your rate limits for the OpenAI model you're using. For example:

```python
from openlimit_lite import ChatRateLimiter

rate_limiter = ChatRateLimiter(request_limit=200, token_limit=40000)
```

This sets a rate limit for a chat completion model (e.g. gpt-4, gpt-3.5-turbo). `openlimit` offers different rate limiter objects for different OpenAI models, all with the same parameters: `request_limit` and `token_limit`. Both limits are measured _per-minute_ and may vary depending on the user.

| Rate limiter            | Supported models                                                                   |
| ----------------------- | ---------------------------------------------------------------------------------- |
| `ChatRateLimiter`       | gpt-4, gpt-4-0314, gpt-4-32k, gpt-4-32k-0314, gpt-3.5-turbo, gpt-3.5-turbo-0301    |
| `CompletionRateLimiter` | text-davinci-003, text-davinci-002, text-curie-001, text-babbage-001, text-ada-001 |
| `EmbeddingRateLimiter`  | text-embedding-ada-002                                                             |

### Apply the rate limit

To apply the rate limit, add a `with` statement to your API calls:

```python
chat_params = {
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello!"}]
}

with rate_limiter.limit(**chat_params):
    response = openai.ChatCompletion.create(**chat_params)
```

Ensure that `rate_limiter.limit` receives the same parameters as the actual API call. This is important for calculating expected token usage.

Alternatively, you can decorate functions that make API calls, as long as the decorated function receives the same parameters as the API call:

```python
@rate_limiter.is_limited()
def call_openai(**chat_params):
    response = openai.ChatCompletion.create(**chat_params)
    return response
```

### Asynchronous requests

Rate limits can be enforced for asynchronous requests too:

```python
chat_params = {
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello!"}]
}

async with rate_limiter.limit(**chat_params):
    response = await openai.ChatCompletion.acreate(**chat_params)
```

### Token counting

Aside from rate limiting, `openlimit` also provides methods for counting tokens consumed by requests.

#### Chat requests

To count the _maximum_ number of tokens that could be consumed by a chat request (e.g. `gpt-3.5-turbo`, `gpt-4`), pass the [request arguments](https://platform.openai.com/docs/api-reference/chat/create) into the following function:

```python
from openlimit.utilities import num_tokens_consumed_by_chat_request

request_args = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "...", "content": "..."}, ...],
    "max_tokens": 15,
    "n": 1
}
num_tokens = num_tokens_consumed_by_chat_requests(**request_args)
```

#### Completion requests

Similar to chat requests, to count tokens for completion requests (e.g. `text-davinci-003`), pass the [request arguments](https://platform.openai.com/docs/api-reference/completions/create) into the following function:

```python
from openlimit.utilities import num_tokens_consumed_by_completion_request

request_args = {
    "model": "text-davinci-003",
    "prompt": "...",
    "max_tokens": 15,
    "n": 1
}
num_tokens = num_tokens_consumed_by_completion_request(**request_args)
```

#### Embedding requests

For embedding requests (e.g. `text-embedding-ada-002`), pass the [request arguments](https://platform.openai.com/docs/api-reference/embeddings/create) into the following function:

```python
from openlimit.utilities import num_tokens_consumed_by_embedding_request

request_args = {
    "model": "text-embedding-ada-002",
    "input": "..."
}
num_tokens = num_tokens_consumed_by_embedding_request(**request_args)
```
