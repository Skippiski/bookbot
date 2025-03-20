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