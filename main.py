def get_book_text(filepath):
    with open(filepath) as f:
     file_contents = f.read()

    return file_contents

def num_words(file_contents):
    words = file_contents.split()
    return len(words)

def main ():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    total_words = num_words(book_text)
    print(book_text,f"{total_words} words found in the document.")


main()