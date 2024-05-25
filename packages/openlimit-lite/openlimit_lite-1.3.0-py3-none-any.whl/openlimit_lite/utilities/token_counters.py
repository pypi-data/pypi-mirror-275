# Third party
from typing import Any, Dict, Iterable, List, Union
import tiktoken

# Tokenizer
CL100K_ENCODER = tiktoken.get_encoding("cl100k_base")
P50K_ENCODER = tiktoken.get_encoding("p50k_base")


######
# MAIN
######


def num_tokens_consumed_by_chat_request(
    messages: Iterable[Any], max_tokens: int = 15, n: int = 1, **kwargs: Dict[str, Any]
) -> int:
    num_tokens = n * max_tokens
    for message in messages:
        num_tokens += (
            4  # Every message follows <im_start>{role/name}\n{content}<im_end>\n
        )
        for key, value in message.items():
            num_tokens += len(CL100K_ENCODER.encode(value))

            if key == "name":  # If there's a name, the role is omitted
                num_tokens -= 1  # Role is always required and always 1 token

    num_tokens += 2  # Every reply is primed with <im_start>assistant

    return num_tokens


def num_tokens_consumed_by_completion_request(
    prompt: Union[str, List[str]],
    max_tokens: int = 15,
    n: int = 1,
    **kwargs: Dict[str, Any]
) -> int:
    num_tokens = n * max_tokens
    if isinstance(prompt, str):  # Single prompt
        num_tokens += len(P50K_ENCODER.encode(prompt))
    elif isinstance(prompt, list):  # Multiple prompts # pyright: ignore
        num_tokens *= len(prompt)
        num_tokens += sum([len(P50K_ENCODER.encode(p)) for p in prompt])
    else:
        raise TypeError(
            "Either a string or list of strings expected for 'prompt' field in completion request."
        )

    return num_tokens


def num_tokens_consumed_by_embedding_request(
    input: Union[str, List[str]], **kwargs: Dict[str, Any]
) -> int:
    if isinstance(input, str):  # Single input
        return len(P50K_ENCODER.encode(input))
    elif isinstance(input, list):  # Multiple inputs # pyright: ignore
        return sum([len(P50K_ENCODER.encode(i)) for i in input])

    raise TypeError(
        "Either a string or list of strings expected for 'input' field in embedding request."
    )
