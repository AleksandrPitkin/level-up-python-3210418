import json  # We use the JSON format for saving and loading the dictionary.


def save_dict(dictionary: dict, file_path: str):
    try:
        with open(file_path, 'w') as file:
            # Use the 'json.dump()' method to write the dictionary to the file in JSON format.
            json.dump(dictionary, file)
        print(f"Dictionary saved to {file_path}")
    except Exception as e:
        print(f"Error saving dictionary: {str(e)}")


def load_dict(file_path: str):
    try:
        with open(file_path, 'r') as file:
            # Use the 'json.load()' method to read the dictionary from the file.
            loaded_dict = json.load(file)
        return loaded_dict
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error loading dictionary: {str(e)}")
    return {}


# Example usage:
if __name__ == "__main__":
    # Test saving a dictionary to a file
    my_dict = {"name": "Alice", "age": 30, "city": "Wonderland"}
    save_dict(my_dict, "my_dict.json")

    # Test loading a dictionary from a file
    loaded_dict = load_dict("my_dict.json")
    print("Loaded Dictionary:", loaded_dict)
