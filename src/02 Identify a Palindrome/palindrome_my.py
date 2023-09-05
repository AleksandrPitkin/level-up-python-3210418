def is_palindrome(phrase):
    # Clean the input phrase by removing non-alphabetic characters and making it lowercase.
    forward = clean_string(phrase)

    # Reverse the cleaned string using slicing.
    backward = forward[::-1]

    # Check if the cleaned string reads the same forwards and backwards.
    return forward == backward


def clean_string(input_string: str):
    # Initialize an empty string to store the cleaned string.
    cleaned_string = ""

    # Iterate through each character in the input string.
    for char in input_string:
        # Check if the character is an alphabetic character (a-z or A-Z).
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            # If it is alphabetic, append it to the cleaned string.
            cleaned_string += char

    # Convert the cleaned string to lowercase to ensure case-insensitive palindrome checking.
    return cleaned_string.lower()


# commands used in solution video for reference
if __name__ == '__main__':

    # Palindromes
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
    print(is_palindrome('racecar'))  # true
    print(is_palindrome('deified'))  # true
    print(is_palindrome('level'))    # true
    print(is_palindrome('A man a plan a canal Panama'))  # true
    print(is_palindrome('Was it a car or a cat I saw?'))  # true
    # true -> empty string
    print(is_palindrome('1234567890'))

    # Non-Palindromes
    print(is_palindrome('hello world'))  # false
    print(is_palindrome('python'))                        # false
    print(is_palindrome('not a palindrome'))              # false
