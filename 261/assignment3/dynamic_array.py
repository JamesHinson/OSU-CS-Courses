# Name: James Hinson
# OSU Email: hinsonj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2
# Due Date: 2/5/2024
# Description: A custom DynamicArray class that has many features.
#              Includes the ability to: merge, map, filter, reduce, slice and resize;
#              find the mode of, append, and remove values at specified indices.


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Changes the underlying storage capacity for the elements in the dynamic array.

        :param new_capacity: The new capacity to set for the dynamic array.
        :return: None
        """
        if new_capacity <= 0:
            return  # Do nothing if new_capacity is not a positive integer

        # Create a new StaticArray with the specified capacity
        new_static_array = StaticArray(new_capacity)

        # Determine the number of elements to copy
        num_elements_to_copy = min(self._size, new_capacity)

        # Copy elements from the current array to the new array
        for i in range(num_elements_to_copy):
            new_static_array.set(i, self.get_at_index(i))

        # Update the dynamic array's capacity and data
        self._capacity = new_capacity
        self._data = new_static_array

        # Update the size to match the number of elements copied
        self._size = num_elements_to_copy


    def append(self, value: object) -> None:
        """
        Adds a new value at the end of the dynamic array. If the array is full, it doubles the capacity before adding.

        :param value: The value to be added to the dynamic array.
        :return: None
        """
        # Check if the array is full and needs resizing
        if self.length() >= self._capacity:
            # Double the capacity using the resize method
            new_capacity = 2 * self._capacity
            self.resize(new_capacity)

        # Add the value to the end of the array
        self._data[self._size] = value
        self._size += 1


    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a new value at the specified index in the dynamic array.

        :param index: The index at which to insert the value.
        :param value: The value to be inserted.
        :return: None
        """
        if not (0 <= index <= self._size):
            raise DynamicArrayException

        # Check if the array is full and needs resizing
        if self.length() >= self._capacity:
            # Double the capacity using the resize method
            new_capacity = 2 * self._capacity
            self.resize(new_capacity)

        # Shift elements to the right to make space for the new value
        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]

        # Set the value at the specified index
        self._data[index] = value
        self._size += 1


    def remove_at_index(self, index: int) -> None:
        """
        Removes the element at the specified index in the dynamic array.

        :param index: The index at which to remove the element.
        :return: None
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException

        # Check if the array needs resizing before removal
        if self._capacity > 10 and self._size <= self._capacity // 4:
            new_capacity = max(self._capacity // 2, 10)
            self.resize(new_capacity)

        # Shift elements to fill the gap
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        # Decrement the size after removal
        self._size -= 1


    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Returns a new DynamicArray object containing the requested number of elements from the original array,
        starting with the element located at the requested start index.

        :param start_index: The start index of the slice.
        :param size: The requested size of the slice.
        :return: DynamicArray object representing the slice.
        """
        if not (0 <= start_index <= self.length() - 1) or size < 0:
            raise DynamicArrayException("Invalid start index or size")

        if start_index + size > self.length():
            raise DynamicArrayException("Not enough elements to make the slice")

        da_slice = DynamicArray()

        i = start_index
        while i < start_index + size:
            da_slice.append(self.get_at_index(i))
            i += 1

        return da_slice


    def merge(self, second_da: "DynamicArray") -> None:
        """
        Appends all elements from the input array onto the current DynamicArray in the same order.

        :param second_da: Another DynamicArray object to be merged.
        :return: None
        """
        for i in range(second_da.length()):
            self.append(second_da.get_at_index(i))


    def map(self, map_func) -> "DynamicArray":
        """
        Creates a new DynamicArray where the value of each element is derived by applying a given map_func
        to the corresponding value from the original array.

        :param map_func: The mapping function to apply to each element.
        :return: DynamicArray object representing the mapped values.
        """
        new_array = DynamicArray()
        i = 0

        while i < self._size:
            new_array.append(map_func(self.get_at_index(i)))
            i += 1

        return new_array


    def filter(self, filter_func) -> "DynamicArray":
        """
        Creates a new DynamicArray populated only with elements from the original array for which filter_func returns True.

        :param filter_func: The filtering function to apply to each element.
        :return: DynamicArray object representing the filtered values.
        """
        filtered_array = DynamicArray()

        for i in range(self.length()):
            element = self.get_at_index(i)
            if filter_func(element):
                filtered_array.append(element)

        return filtered_array


    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Sequentially applies the reduce_func to all elements of the dynamic array and returns the resulting value.

        :param reduce_func: The reducing function to apply to each pair of elements.
        :param initializer: Optional initializer parameter.
        :return: Resulting value after applying the reducing function.
        """

        # If the dynamic array is empty, return the provided initializer
        if self.is_empty():
            return initializer

        # If the initializer is not provided, initialize it with the first element of the array
        if initializer is None:
            initializer = self._data[0]

            # Iterate over the remaining elements of the array
            for i in range(self.length() - 1):

                # Apply the reduce_func to the current initializer and the next element in the array
                initializer = reduce_func(initializer, self._data[i + 1])

            # Return the resulting initializer
            return initializer

        # If the initializer is provided, apply the reduce_func to the initializer and the first element of the array
        initializer = reduce_func(initializer, self._data[0])

        # Iterate over the remaining elements of the array
        for i in range(self.length() - 1):

            # Apply the reduce_func to the current initializer and the next element in the array
            initializer = reduce_func(initializer, self._data[i + 1])

        # Return the resulting initializer
        return initializer


def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    """
    Finds the mode (most-occurring values) and its frequency in a sorted DynamicArray.

    :param arr: A DynamicArray in sorted order.

    :return: A tuple containing a DynamicArray comprising the mode values and an integer
             representing the highest frequency (how many times they appear).
    """

    # Initialize variables to track mode and frequency
    current_mode = arr[0]
    current_frequency = 1
    max_frequency = 1
    
    # Initialize mode dynamic array
    mode_da = DynamicArray()
    mode_da.append(current_mode)
    
    # Iterate through the array starting from the second element
    for i in range(1, arr.length()):
        if arr[i] == arr[i - 1]:
            # If current element equals previous element, increase frequency
            current_frequency += 1

        else:
            # If current element is different, update mode and frequency
            current_mode = arr[i]
            current_frequency = 1
        
        # Update max frequency
        if current_frequency > max_frequency:
            max_frequency = current_frequency
            mode_da = DynamicArray()  # Clear previous mode
            mode_da.append(current_mode)

        elif current_frequency == max_frequency:
            mode_da.append(current_mode)  # Append current mode
        
    return mode_da, max_frequency


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
