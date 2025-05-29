from stats import get_word_count

def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def main():
    file_contents = get_book_text()
    num_words = get_word_count(file_contents)
    print(f"{num_words} words found in the document")

main()