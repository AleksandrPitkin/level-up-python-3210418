def index_all(objects: list, item_to_find):
    index_list = []  # Initialize an empty list to store indices

    # Iterate through each element (item) in the 'objects' list
    for index, item in enumerate(objects):

        # Check if the current item is equal to the item to find
        if item == item_to_find:
            index_list.append([index])  # Append the current index as a list

        # Check if the current item is a nested list
        if isinstance(item, list):
            # If the item is a list, recursively search within it
            sub_indices = index_all(item, item_to_find)
            for i in sub_indices:
                # Append the current index along with sub-indices to the index_list
                index_list.append([index] + i)

    return index_list


# commands used in solution video for reference
if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]
    # [[0, 0], [1]]
    print(index_all([1, [2, 3, [4]], [5, 6], [7, [8, 9]]], 4))
    # [[1, 2, 0]]
