def get_book_text(filepath):
    with open(filepath) as f:
     file_contents = f.read()

    return file_contents

from stats import num_words, letter_count

def main ():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words1 = num_words(book_text)
    letter_count1 = letter_count(book_text)
    print(book_text,letter_count1,f"{num_words1} words found in the document.")


main()