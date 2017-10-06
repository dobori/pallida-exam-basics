# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]


def unique_characters(word):
    try:
        list_of_chars = []
        if word == None:
            word = 0
        for letter in word:
            if letter not in list_of_chars:
                list_of_chars.append(letter)
            elif letter in list_of_chars:
                must_deleting = []
                must_deleting.append(letter)
        for deleting_letter in must_deleting:
            if deleting_letter in list_of_chars:
                list_of_chars.remove(deleting_letter)
        return list_of_chars

    except Exception:
        return False



    