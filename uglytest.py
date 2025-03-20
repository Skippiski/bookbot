def get_book_text(filepath):
    with open(filepath) as f:
     file_contents = f.read()

    return file_contents

def num_words(file_contents):
    words = file_contents.split()
    return len(words)

def letter_count(file_contents):
    counted_letters = {}
    for i in file_contents:
        i =i.lower()
        if i in counted_letters:
             counted_letters[i] += 1
        else:
            counted_letters[i] = 1
    return counted_letters

def main ():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words1 = num_words(book_text)
    letter_count1 = letter_count(book_text)
    print(book_text,letter_count1,f"{num_words1} words found in the document.")

if __name__ == "__main__":
    main()