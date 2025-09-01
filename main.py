def get_book_text():
    with open(path_to_file) as f:
        file_contents = f.read()  
    return file_contents

def main():
    contents = get_book_text("./books/frankenstein.txt")
    print(contents)
    return

main()