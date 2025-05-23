import sys
from stats import get_num_words, get_character_count, get_sorted_char_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_count = get_character_count(book_text)
    sorted_chars = get_sorted_char_list(char_count)
    
    print(f"Found {num_words} total words")
    print()
    
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")

main()



