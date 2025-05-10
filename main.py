import sys
from stats import count_words, count_characters, sort_char_counts

def get_book_text(filepath):
    """Read and return the entire text from the given file path."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
    
def usage_and_exit():
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    # Must pass exactly one argument: the path to the book
    if len(sys.argv) != 2:
        usage_and_exit()

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    # Read and analyze
    text = get_book_text(book_path)
    num_words = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    # Character count
    char_counts = count_characters(text)
    sorted_chars = sort_char_counts(char_counts)
    
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    
    print("============= END ===============")

if __name__ == '__main__':
    main()
