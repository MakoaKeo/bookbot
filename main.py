def get_book_text():
    with open("~/github/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()  

def main():
    get_book_text()

main()