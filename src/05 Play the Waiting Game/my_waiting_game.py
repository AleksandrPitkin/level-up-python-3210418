import random
import time


def waiting_game():
    # Set a random delay time between 2 and 4 seconds
    delay = random.randint(2, 4)

    # Print a message asking the player
    print(f"Ready to start the Game?\n Your target time is {delay}!")

    # Start the timer
    input(' ---Press Enter to Begin--- ')
    start_time = time.perf_counter()
    
    input(f'Press Enter again after {delay} seconds...')

    # Calculate the elapsed time
    elapsed_time = round(time.perf_counter() - start_time, 2)

    # Check if the player waited long enough
    if elapsed_time >= delay:
        print(
            f"Well done! You waited {elapsed_time} seconds, which is exactly what you were asked to do.")
    elif elapsed_time < delay:
        print(
            f"Oops, you were too quick! You only waited {elapsed_time} seconds, when you were supposed to wait {delay} seconds.")
    else:
        print(
            f"You took too long! You waited {elapsed_time} seconds, but you were only supposed to wait {delay} seconds.")


# commands used in solution video for reference
if __name__ == '__main__':
    waiting_game()

