from functools import lru_cache

from pymentoring.utils.string_utils import assert_valid_str
from .constants import LRU_CACHE_SIZE


@lru_cache(maxsize=LRU_CACHE_SIZE)
def get_unique_chars(input_string: str) -> list[str]:
    valid_input_string = assert_valid_str(input_string)
    char_counter = {}

    for char in valid_input_string:
        char_counter[char] = char_counter.get(char, 0) + 1

    unique_chars = [char for char, count in char_counter.items() if count == 1]
    return unique_chars
