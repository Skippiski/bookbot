import sys

from stats import num_words, letter_count,sort_on, sortCL

def get_book_text(filepath):
     with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main ():

    if len(sys.argv) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words1 = num_words(book_text)
    letter_counts= letter_count(book_text)
    sorted_chars = sortCL(letter_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words1} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

    
main()