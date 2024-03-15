# Name: James Hinson
# OSU Email: hinsonj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 6
# Due Date: 3/14/24
# Description: Assignment 6 - Open Addressing HashMap

from a6_include import (DynamicArray, DynamicArrayException, HashEntry,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        quadratic probing for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(None)

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
        Increment from given number to find the closest prime number
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
        Updates the key/value pair. Resizes if load factor >= 0.5.
        """
        # Check if resizing is necessary
        if self.table_load() >= 0.5:
            self.resize_table(2 * self._capacity)

        # Compute the hash of the key
        hash_value = self._hash_function(key)
        initial_index = hash_value % self._capacity
        index = initial_index

        # Handle collisions using quadratic probing
        if self._buckets[index] is not None:
            j = 0
            while self._buckets[index] is not None:
                # If key already exists, update its value
                if self._buckets[index].key == key and not self._buckets[index].is_tombstone:
                    self._buckets[index].value = value
                    return
                # If tombstone is encountered, insert new key-value pair
                if self._buckets[index].is_tombstone:
                    self._buckets[index] = HashEntry(key, value)
                    self._size += 1
                    return
                else:
                    j += 1
                    index = (initial_index + j**2) % self.get_capacity()

        # Insert key-value pair into an empty bucket
        self._buckets[index] = HashEntry(key, value)
        self._size += 1


    def resize_table(self, new_capacity: int) -> None:
        """
        Resizes the hash map's underlying table to the specified capacity.

        If the new capacity is less than the current size, no resizing occurs.
        """
        # Check if new capacity is less than current size
        if new_capacity < self._size:
            return

        # Set capacity to new_capacity if prime, otherwise set it to next prime
        self._capacity = new_capacity if self._is_prime(new_capacity) else self._next_prime(new_capacity)

        # Store current buckets in temp variable
        temp = self._buckets

        # Create a new empty DynamicArray for buckets and reset size to 0
        self._buckets = DynamicArray()
        self._size = 0

        # Append None to new bucket array up to the new capacity
        for index in range(self._capacity):
            self._buckets.append(None)

        # Re-add elements from temp into resized bucket array
        for index in range(temp.length()):
            if temp[index] is not None and not temp[index].is_tombstone:
                # Re-hash and re-insert non-tombstone elements into new array
                self.put(temp[index].key, temp[index].value)


    def table_load(self) -> float:
        """
        Returns the hash table load factor.
        """
        return self._size / self._capacity


    def empty_buckets(self) -> int:
        """
        Counts the number of empty buckets in the hash map.
        """
        return self._capacity - self._size


    def get(self, key: str):
        """
        Retrieves the value associated with the given key.

        If the key is found and not marked as a tombstone, return its associated value. 
        If the key is not found or is marked as a tombstone, return None.
        """
        # Calculate hash and initial index for the key
        hash_value = self._hash_function(key)
        initial_index = hash_value % self._capacity

        j = 0
        index = initial_index

        # Search for the key using quadratic probing
        while self._buckets[index] is not None:
            # Check if the current bucket contains the key and is not a tombstone
            if self._buckets[index].key == key and not self._buckets[index].is_tombstone:
                # Return the value associated with the key
                return self._buckets[index].value

            # Increment the quadratic probing counter and calculate the next index
            j += 1
            index = (initial_index + j ** 2) % self.get_capacity()

        # If key is not found or is marked as a tombstone, return None
        return None


    def contains_key(self, key: str) -> bool:
        """
        Checks if the hash map contains the specified key.

        Returns True if the key is found in the hash map, otherwise returns False.
        """
        # If the hash map is empty, the key cannot exist
        if self._size == 0:
            return False

        # Check if the key exists in the hash map by attempting to retrieve its value
        if self.get(key) is None:
            return False

        # If the key is found, return True
        return True


    def remove(self, key: str):
        """
        Removes the key-value pair associated with the specified key from the hash map.

        If the key exists in the hash map, mark its corresponding bucket as a tombstone to indicate
        that it has been removed. Decrease the size of the hash map accordingly.
        """
        # Calculate the hash and initial index for the key
        hash = self._hash_function(key)
        initial_index = hash % self._capacity
        index = initial_index
        j = 0

        # Search for the key in the hash map
        while self._buckets[index] is not None:
            if self._buckets[index].key == key and self._buckets[index].is_tombstone is False:
                # Mark the bucket as a tombstone to indicate removal and decrease the size
                self._buckets[index].is_tombstone = True
                self._size -= 1
            j += 1
            index = (initial_index + j ** 2) % self.get_capacity()


    def get_keys_and_values(self):
        """
        Retrieves all key-value pairs stored in the hash map.

        Returns a DynamicArray containing tuples of keys and corresponding values.
        Each tuple represents a key-value pair stored in the hash map.
        """
        # Create a DynamicArray to store key-value pairs
        keys_and_values = DynamicArray()

        # Iterate through the buckets in the hash map
        for index in range(self._buckets.length()):
            # Check if the bucket contains a valid key-value pair
            if self._buckets[index] is not None and self._buckets[index].is_tombstone is False:
                # Append the key-value pair to the DynamicArray
                keys_and_values.append((self._buckets[index].key, self._buckets[index].value))

        return keys_and_values


    def clear(self):
        """
        Removes all key-value pairs from the hash map.

        Resets the hash map's underlying DynamicArray to contain only None values,
        effectively clearing all stored key-value pairs.
        """
        # Reset the hash map's DynamicArray to contain only None values
        self._buckets = DynamicArray()
        for index in range(self._capacity):
            self._buckets.append(None)
        # Reset the size of the hash map to zero
        self._size = 0


    def __iter__(self):
        """
        Initializes the iterator for the hash map.

        Resets the iterator's index to 0 to start iterating from the beginning of the hash map.
        """
        # Reset the iterator's index to 0
        self._index = 0
        # Return the initialized iterator
        return self


    def __next__(self):
        """
        Returns the next non-tombstone hash entry in the hash map.

        If there are no more non-tombstone entries, raises StopIteration.
        """
        # Iterate through the hash map's buckets
        while self._index < self._capacity:

            # Check if the current bucket is not empty and not a tombstone
            if self._buckets[self._index] is not None and self._buckets[self._index].is_tombstone is False:
                # Store the current bucket's value
                value = self._buckets[self._index]
                self._index += 1
                return value

            # Move to the next bucket
            self._index += 1

        # If there are no more non-tombstone entries, raise StopIteration
        raise StopIteration


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
    keys = [i for i in range(25, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        if m.table_load() > 0.5:
            print(f"Check that the load factor is acceptable after the call to resize_table().\n"
                  f"Your load factor is {round(m.table_load(), 2)} and should be less than or equal to 0.5")

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
    m = HashMap(11, hash_function_1)
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

    m.resize_table(2)
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(12)
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

    print("\nPDF - __iter__(), __next__() example 1")
    print("---------------------")
    m = HashMap(10, hash_function_1)
    for i in range(5):
        m.put(str(i), str(i * 10))
    print(m)
    for item in m:
        print('K:', item.key, 'V:', item.value)

    print("\nPDF - __iter__(), __next__() example 2")
    print("---------------------")
    m = HashMap(10, hash_function_2)
    for i in range(5):
        m.put(str(i), str(i * 24))
    m.remove('0')
    m.remove('4')
    print(m)
    for item in m:
        print('K:', item.key, 'V:', item.value)
