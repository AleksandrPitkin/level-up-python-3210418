def get_prime_factors(number):
    factors_list = []  # Initialize an empty list to store the prime factors.
    divide = 2  # Start from 2, as 1 is not considered a prime factor.

    while divide <= number:
        if number % divide == 0:
            # If 'number' is divisible by 'divide', it means 'divide' is a prime factor.
            # Add 'divide' to the list of prime factors.
            factors_list.append(divide)
            # Divide 'number' by 'divide' to update its value.
            number //= divide
        else:
            # If 'divide' is not a factor, increment it to check the next number.
            divide += 1

    # Return the list of prime factors of the input 'number'.
    return factors_list




# commands used in solution video for reference
if __name__ == '__main__':
    print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]
