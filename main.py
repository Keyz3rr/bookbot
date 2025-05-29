from stats import get_word_count, get_num_characters, sort_char_count

import sys

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    num_words = get_word_count(file_contents)
    character_count = get_num_characters(file_contents)
    characters = sort_char_count(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in characters:
        char_key = char["char"]
        char_count = char["num"]
        print(f"{char_key}: {char_count}")
    print("============= END ===============")

main()