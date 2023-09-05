def sort_words(words):
    # Initialize an empty string to store the sorted words.
    new_words = ""

    # Split the input 'words' into a list of words.
    words_list = words.split()

    # Sort the list of words alphabetically with case-insensitivity.
    words_list = sorted(words_list, key=str.lower)

    # Iterate through the sorted words and build a new string.
    for w in words_list:
        # Append the current word to the 'new_words' string.
        new_words += w
        # Add a space after each word to separate them.
        new_words += " "

    # Remove the trailing space and return the sorted string.
    return new_words[:len(new_words) - 1]


# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
    print(sort_words(''))  # ''
    print(sort_words('Dog cat bird'))  # bird cat Dog
    print(sort_words('The quick brown fox jumps over the lazy dog'))
    # brown dog fox jumps lazy over quick The the
    
