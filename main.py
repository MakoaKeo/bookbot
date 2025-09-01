def get_book_text():
    with open("frankenstein.txt") as f:
        file_contents = f.read()  

def main():
    get_book_text()

main()