def roll_dice(*dice_sides):
    
    def recursive_probability(dice_index, current_total, probabilities):
        if dice_index == len(dice_sides):
            # If we have considered all dice, update the probability table
            probabilities[current_total] += 1
        else:
            for outcome in range(1, dice_sides[dice_index] + 1):
                # Recursively calculate probabilities for all possible outcomes
                recursive_probability(
                    dice_index + 1, current_total + outcome, probabilities)

    # Initialize a dictionary to store probabilities for each possible total
    probabilities = {}
    max_total = sum(dice_sides)

    for total in range(len(dice_sides), max_total + 1):
        probabilities[total] = 0

    # Calculate probabilities using recursion
    recursive_probability(0, 0, probabilities)

    # Calculate the total number of possible outcomes
    total_outcomes = sum(probabilities.values())

    # Print the probability table
    print(f"\n{'Total':<10} {'Probability':<15}")
    for total, count in probabilities.items():
        probability = count / total_outcomes * 100
        print(f"{total:<10} {probability:0.2f}%")


# Example usage:
if __name__ == "__main__":
    roll_dice(4, 6, 6)
    roll_dice(4, 6, 6, 20)
