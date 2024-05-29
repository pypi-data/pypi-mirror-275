import tiktoken
from ._types import GPTModel


def num_tokens_from_string(string: str,model: GPTModel = None) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def num_token_from_message(message: dict, model: GPTModel = None) -> int:
    """Returns the number of tokens in a message."""
    return num_tokens_from_string(message["content"], model)
