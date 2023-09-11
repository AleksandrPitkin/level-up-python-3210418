import time


def schedule_function(execution_time, func, *args):
    
    current_time = time.time()

    # Calculate the delay (in seconds) until the scheduled execution time.
    delay = max(0, execution_time - current_time)

    # Print a message indicating the scheduled function and execution time.
    print(
        f"Scheduling function '{func.__name__}' to run at {time.ctime(execution_time)}")

    # Sleep for the calculated delay.
    time.sleep(delay)

    # Execute the function with provided arguments and keyword arguments.
    func(*args)

# Example usage:


# commands used in solution video for reference
if __name__ == '__main__':
    schedule_function(time.time() + 1, print, 'Howdy!')
    schedule_function(time.time() + 1, print, 'Howdy!', 'How are you?')
