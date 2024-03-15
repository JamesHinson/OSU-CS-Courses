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
        Updates the key/value pair in the hash map. If the given key already exists in
        the hash map, its associated value is replaced with the new value. If the given
        key is not in the hash map, a new key/value pair is added.
        If the current load factor of the table is greater than or equal to 0.5 after
        putting the new key/value pair, the table is resized to double its current capacity.
        """
        # Calculate the index for the key
        index = self._hash_function(key) % self._capacity
        
        # Check if the key already exists in the hash map
        if self._buckets[index] is not None and self._buckets[index].key == key:
            # Update the value for the existing key
            self._buckets[index].value = value
        else:
            # Insert the key-value pair into the hash map
            self._buckets[index] = HashEntry(key, value)
            self._size += 1
            
            # Check if resizing is needed
            load_factor = self.table_load()
            if load_factor >= 0.5:
                new_capacity = self._capacity * 2
                self.resize_table(new_capacity)


    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the hash map's underlying table. All active key/value pairs
        are put into the new table, meaning all non-tombstone hash table links are rehashed.
        """
        # Check if new_capacity is less than the current number of elements
        if new_capacity < self._size:
            return

        # Create a new dynamic array with the specified new_capacity
        new_buckets = DynamicArray()

        # Increment new_capacity to the next prime number
        new_capacity = self._next_prime(new_capacity)

        # Populate the new dynamic array with None values
        for _ in range(new_capacity):
            new_buckets.append(None)

        # Rehash and insert each non-empty bucket into the new dynamic array
        for entry in self._buckets:
            if entry is not None:
                new_index = self._hash_function(entry.key) % new_capacity
                while new_buckets[new_index] is not None:
                    # Quadratic probing
                    new_index = (new_index + 1) % new_capacity
                new_buckets[new_index] = entry

        # Update the hash map's capacity and buckets
        self._capacity = new_capacity
        self._buckets = new_buckets


    def table_load(self) -> float:
        """
        Returns the current hash table load factor.
        """
        if self._capacity > 0:
            return self._size / self._capacity
        else:
            return 0.0


    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the hash map.
        """
        empty_count = 0

        for bucket in self._buckets:
            if bucket is None:
                empty_count += 1
        return empty_count


    def get(self, key: str) -> object:
        """
        Returns the value associated with the given key.
        If the key is not found, returns None.
        """
        index = self._hash_function(key) % self._capacity
        start_index = index

        while self._buckets[index] is not None:
            if self._buckets[index].key == key:
                return self._buckets[index].value
            index = (index + 1) % self._capacity
            if index == start_index:
                break
        return None


    def contains_key(self, key: str) -> bool:
        """
        Returns True if the given key exists in the hash map, otherwise returns False.
        """
        index = self._hash_function(key) % self._capacity
        start_index = index
        while self._buckets[index] is not None:
            if self._buckets[index].key == key:
                return True
            index = (index + 1) % self._capacity
            if index == start_index:
                break
        return False


    def remove(self, key: str) -> None:
        """
        Removes the key-value pair associated with the given key from the hash map.
        """
        index = self._hash_function(key) % self._capacity
        start_index = index

        while self._buckets[index] is not None:
            if self._buckets[index].key == key:
                self._buckets[index] = HashEntry(None, None, True)  # Tombstone
                self._size -= 1
                return
            index = (index + 1) % self._capacity
            if index == start_index:
                break


    def get_keys_and_values(self) -> DynamicArray:
        """
        Returns a dynamic array containing all key-value pairs in the hash map.
        """
        key_value_pairs = DynamicArray()

        for entry in self._buckets:
            if entry and not entry.is_tombstone:
                key_value_pairs.append((entry.key, entry.value))

        return key_value_pairs


    def clear(self) -> None:
        """
        Removes all key-value pairs from the hash map.
        """
        for i in range(self._capacity):
            self._buckets[i] = None
        self._size = 0


    def __iter__(self):
        """
        Enables iteration over the hash map.
        """
        self._iter_index = 0
        return self

    def __next__(self):
        """
        Returns the next non-empty HashEntry object in the hash map.
        """
        while self._iter_index < self._capacity:
            entry = self._buckets[self._iter_index]
            self._iter_index += 1
            if entry is not None and not entry.is_tombstone():
                return entry
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
