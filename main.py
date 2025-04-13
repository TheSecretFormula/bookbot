import sys
from stats import word_count, character_count, sort_on, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)

    number_of_words = word_count(book_text)
    char_counts = character_count(book_text)
    sorted_chars = sort_chars(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    
    print("--------- Character Count -------")
    for char_info in sorted_chars:
        char = char_info["char"]
        count = char_info["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()