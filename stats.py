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