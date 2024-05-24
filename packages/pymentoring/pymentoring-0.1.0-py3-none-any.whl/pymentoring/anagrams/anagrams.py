from pymentoring.utils.string_utils import assert_valid_str


def make_anagram_from_text(text: str) -> str:
    valid_text = assert_valid_str(text)
    words = [reverse_letters_in_place(word) for word in valid_text.split(" ")]
    return ' '.join(words)


def reverse_letters_in_place(word: str) -> str:
    valid_word = assert_valid_str(word)
    letters = [c for c in valid_word if c.isalpha()][::-1]
    reversed_word = (letters.pop(0) if c.isalpha() else c for c in valid_word)
    return ''.join(reversed_word)
