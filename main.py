from stats import get_num_words, get_character_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    letter_count = get_character_count(text)
    num_words = get_num_words(text)
    print(f"{num_words} found in the document")
    print(letter_count)



def get_book_text(path):
    with open(path) as f:
        body = f.read()
        return body


main()