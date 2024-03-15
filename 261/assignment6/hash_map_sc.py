# Name: James Hinson
# OSU Email: hinsonj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 6
# Due Date: 3/14/24
# Description: Assignment 6 - Separate Chaining HashMap


from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        Updates the key/value pair. Resizes if load factor >= 1.
        """
        # Resize if load factor is 1 or greater
        if self.table_load() >= 1:
            self.resize_table(2 * self._capacity)

        # Calculate hash and index for the key
        hash_value = self._hash_function(key)
        index = hash_value % self._capacity

        # Update or insert key/value pair
        existing_node = self._buckets[index].contains(key)

        if existing_node is not None:
            existing_node.value = value
        else:
            self._buckets[index].insert(key, value)
            self._size += 1


    def resize_table(self, new_capacity: int) -> None:
        """
        Resizes the hash table to the specified new capacity.
        """
        # Do nothing if new_capacity is less than 1
        if new_capacity < 1:
            return

        # Set new capacity to the next prime number if it isn't already prime
        if not self._is_prime(new_capacity):
            new_capacity = self._next_prime(new_capacity)

        self._capacity = new_capacity

        # Store current data for rehashing
        temp_buckets = self._buckets

        # Reset bucket list and size
        self._buckets = DynamicArray()
        self._size = 0

        # Fill new bucket list with empty linked lists
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        # Rehash key/value pairs into new bucket list
        for index in range(temp_buckets.length()):
            if temp_buckets[index].length() != 0:
                for node in temp_buckets[index]:
                    self.put(node.key, node.value)


    def table_load(self) -> float:
        """
        Returns the hash table load factor
        """
        return self._size / self._capacity


    def empty_buckets(self) -> int:
        """
        Counts the number of empty buckets in the hash map.
        """
        empty_count = 0

        # Count empty buckets
        for index in range(self._buckets.length()):
            if self._buckets[index].length() == 0:
                empty_count += 1

        return empty_count


    def get(self, key: str):
        """
        Returns the value associated with the given key, or None if the key is not found.
        """
        # Calculate index using hash function
        hash_value = self._hash_function(key)
        index = hash_value % self._capacity

        # Check if key exists in the bucket
        if self._buckets[index].contains(key) is None:
            return None

        # Return the value associated with the key
        return self._buckets[index].contains(key).value


    def contains_key(self, key: str) -> bool:
        """
        Check if the hash map contains the specified key.

        Return True if the key is found in the hash map, otherwise return False.
        """
        # If the hash map is empty, the key cannot exist
        if self._size == 0:
            return False

        # Check if the key exists in the hash map by attempting to retrieve its value
        if self.get(key) is None:
            return False

        # If the key is found, return True
        return True


    def remove(self, key: str) -> None:
        """
        Removes the key-value pair associated with the given key.
        """
        # Calculate the index for the key
        hash_value = self._hash_function(key)
        index = hash_value % self._capacity

        # Remove the key-value pair if it exists
        if self._buckets[index].remove(key):
            self._size -= 1


    def get_keys_and_values(self) -> DynamicArray:
        """
        Returns a DynamicArray containing tuples of keys and values.
        """
        keys_values = DynamicArray()

        for index in range(self._buckets.length()):
            # Check if the bucket is not empty
            if self._buckets[index].length() != 0:
                # Iterate through each node in the bucket
                for node in self._buckets[index]:
                    # Append a tuple of key and value to the DynamicArray
                    keys_values.append((node.key, node.value))

        return keys_values
        

    def clear(self) -> None:
        """
        Clears all key-value pairs from the hash map.
        """
        # Reset each bucket to an empty linked list
        for index in range(self._buckets.length()):
            self._buckets[index] = LinkedList()

        self._size = 0


def find_mode(da: DynamicArray) -> tuple[DynamicArray, int]:
    """
    Finds the mode(s) and their frequency in the given DynamicArray.
    """
    map = HashMap()

    # Count frequencies of elements in the DynamicArray
    for index in range(da.length()):
        if map.contains_key(da[index]):
            map.put(da[index], map.get(da[index]) + 1)
        else:
            map.put(da[index], 1)

    mode = DynamicArray()
    mode_frequency = 0
    key_value_pairs = map.get_keys_and_values()

    # Iterate through key-value pairs in the HashMap
    for index in range(key_value_pairs.length()):
        # Retrieve element and frequency from the key-value pair
        element, frequency = key_value_pairs[index]

        # Compare frequencies to determine mode(s)
        if frequency == mode_frequency:
            mode.append(element)
        elif frequency > mode_frequency:
            mode_frequency = frequency
            mode = DynamicArray()
            mode.append(element)

    return mode, mode_frequency


# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(53, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
    print(m.get_keys_and_values())

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")
