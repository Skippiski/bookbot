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
        if not i.isalpha():
            continue
        if i in counted_letters:
             counted_letters[i] += 1
        else:
            counted_letters[i] = 1
    return counted_letters

def sort_on(dict):
    return dict["count"]


def sortCL(counted_letters):
    fully_sorted = []
    for char, count in counted_letters.items():
        char_dict = {"char": char, "count" :count}
        fully_sorted.append(char_dict)
    fully_sorted.sort (reverse=True, key=sort_on)

    return fully_sorted
    


def main ():
    filepath = "books/frankenstein.txt"
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