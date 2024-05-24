import tiktoken


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def num_token_from_message(message: dict, encoding_name: str) -> int:
    """Returns the number of tokens in a message."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(message["content"]))
    return num_tokens
