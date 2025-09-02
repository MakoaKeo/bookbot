def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def find_word_count(path):
    book_text = []
    num_words = []
    
    for word in story:
        book_text.append(word)
    num_words.append(len(book_text))

    print(f"{num_words} words found in the document")




main()