import sys
from stats import return_num_words, count_chars, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main ():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    header = "============ BOOKBOT ============"
    footer = "============= END ==============="

    print(header)
    print(f"Analyzing book found at {book_path}")

    print("----------- Word Count ----------")
    num_words = return_num_words(book_path)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = count_chars(text)
    sorted_chars = sort_chars(char_counts)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]

        if char.isalpha():
            print(f"{char}: {count}")

    print(footer)

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()
