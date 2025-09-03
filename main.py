import sys
from stats import get_num_words, get_character_count, get_sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    letter_count = get_character_count(text)
    num_words = get_num_words(text)
    sorted_list = get_sorted_list(letter_count)

    print(f"{num_words} found in the document")
    print(letter_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")


def get_book_text(path):
    with open(path) as f:
        body = f.read()
        return body


main()