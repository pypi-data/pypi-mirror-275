import sys

from pymentoring.anagrams.anagrams import reverse_letters_in_place

test_data = ["a1aa", "b1b2b", "1c2c3c", 99, True, 0.1, ""]


def get_next_input(prompt):
    if 'coverage' in sys.modules:
        print(prompt)
        return test_data.pop(0)
    else:
        return input(prompt)


def main():
    while True:
        try:
            text = get_next_input("Please enter a string (leave empty to stop): ")
            if not text:
                break
            print(reverse_letters_in_place(text))
        except TypeError as e:
            print("Invalid input, " + str(e))


if __name__ == "__main__":
    main()
