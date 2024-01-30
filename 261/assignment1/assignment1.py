# Name: James Hinson
# OSU Email: hinsonj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 1
# Due Date: 1/29/2024
# Description: Assignment 1 is a series of 10 coding challenges designed to be a review
#              for the Python language, along with several important computer science topics


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """
    Find the minimum and maximum values in a given StaticArray.
    """

    min = arr[0]
    max = arr[arr.length() - 1]

    for index in range(arr.length()):

        if arr[index] < min:
            min = arr[index]

        if arr[index] > max:
            max = arr[index]

    return (min, max)

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Applies FizzBuzz logic to the elements in the arr[] StaticArray.
    Replaces multiples of 3 with 'Fizz', multiples of 5 with 'Buzz',
    and multiples of both 3 and 5 with 'FizzBuzz'
    """

    for index in range(arr.length()):

        current_value = arr[index]

        if (current_value % 3 == 0) and (current_value % 5 == 0):
            arr[index] = 'FizzBuzz'

        elif (current_value % 3) == 0:
            arr[index] = 'Fizz'


        elif (current_value % 5) == 0:
            arr[index] = 'Buzz'


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Reverse the elements in the StaticArray in-place.
    """

    start_index = 0
    end_index = arr.length() - 1

    while start_index < end_index:
        # Swap elements at start_index and end_index
        temp = arr[start_index]
        arr[start_index] = arr[end_index]
        arr[end_index] = temp

        # Move the pointers towards the center
        start_index += 1
        end_index -= 1

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Rotate elements in the StaticArray to the right (if positive) by a number of steps. 
    Rotate elements in the StaticArray to the left (if negative) by a number of steps. 
    """

    length = arr.length()

    # Calculate the effective number of steps to avoid unnecessary rotations
    effective_steps = steps % length

    # Create a new array to store the rotated elements
    rotated_arr = StaticArray(length)

    # Copy the elements from the original array to the rotated array
    for index in range(length):
        rotated_index = (index - effective_steps) % length
        rotated_arr[rotated_index] = arr.get(index)

    return rotated_arr


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    Creates a StaticArray containing integers from start to end (inclusive).
    Supports both ascending and descending ranges.
    """

    # Check if the range should be ascending or descending
    if start <= end:
        # Ascending range
        size = end - start + 1

        result = StaticArray(size)

        # Iterates through the array, calculating the value for each index
        # based on the start value and the current index
        for i in range(size):
            result[i] = start + i

    else:
        # Descending range
        size = start - end + 1

        result = StaticArray(size)

        # Iterates through the array, calculating the value for each index
        # based on the start value and the current index
        for i in range(size):
            result[i] = start - i

    return result

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Checks if the StaticArray is sorted.
    Returns 1 if the array is sorted in strictly ascending order,
    -1 if sorted in strictly descending order, and 0 otherwise.
    """

    length = arr.length()

    # Check for strictly ascending order
    ascending = all(arr[i] <= arr[i + 1] for i in range(length - 1))
    if ascending:
        return 1

    # Check for strictly descending order
    descending = all(arr[i] >= arr[i + 1] for i in range(length - 1))
    if descending:
        return -1

    # If the array isn't strictly ascending or descending, then the array is not sorted
    return 0


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    Finds the mode (most-occurring element) and its frequency in a StaticArray.
    """

    # Initialize variables to keep track of the current mode and its frequency
    current_mode = None
    current_frequency = 0

    # Initialize variables for the current element and its frequency
    current_element = None
    current_element_frequency = 0

    # Iterate through the array to find the mode
    for index in range(arr.length()):
        element = arr[index]

        # If the current element is the same as the previous one, increase its frequency
        if element == current_element:
            current_element_frequency += 1
        else:
            # Update the current element and its frequency
            current_element = element
            current_element_frequency = 1

        # Update the current mode and frequency if needed
        if current_element_frequency > current_frequency:
            current_mode = current_element
            current_frequency = current_element_frequency

    return (current_mode, current_frequency)

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Remove duplicate elements from an array
    """

    # Store unique elements
    unique_arr = StaticArray(arr.length())

    # Keep track of the last inserted index in the unique array
    unique_index = 0

    # Iterate through the input array
    for i in range(arr.length()):
        current_element = arr[i]

        # Check if the element is not already in the unique array
        is_duplicate = False
        for j in range(unique_index):
            if unique_arr[j] == current_element:
                is_duplicate = True
                break

        # If it's not a duplicate, add it to the unique array and update the index
        if not is_duplicate:
            unique_arr[unique_index] = current_element
            unique_index += 1

    # Create a new StaticArray with the new size
    result = StaticArray(unique_index)

    # Copy the unique elements to the result array
    for i in range(unique_index):
        result[i] = unique_arr[i]

    return result

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray and returns a new StaticArray with the same content
    sorted in non-ascending order
    """

    # Check if the array is empty; if so, there's nothing to sort
    if arr.length() == 0:
        return arr

    min_val = float('inf')
    max_val = float('-inf')

    # Find the minimum and maximum values in the array
    for i in range(arr.length()):
        current_element = arr[i]

        min_val = min(min_val, current_element)
        max_val = max(max_val, current_element)

    # Count the occurrences of all elements
    count_arr_size = (max_val - min_val + 1)

    count_arr = StaticArray(count_arr_size)

    for i in range(arr.length()):
        count_arr[arr[i] - min_val] += 1

    # Compute the count of all elements
    for i in range(1, count_arr_size):
        count_arr[i] += count_arr[i - 1]

    # Create the new sorted array
    sorted_arr = StaticArray(arr.length())

    # Iterate over the elements in reverse order, starting at the end
    for i in range((arr.length() - 1), -1, -1):
        current_element = arr[i]

        count_index = current_element - min_val

        sorted_index = count_arr[count_index] - 1

        sorted_arr[sorted_index] = current_element

        count_arr[count_index] -= 1

    return sorted_arr

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
