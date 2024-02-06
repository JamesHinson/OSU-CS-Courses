# Name: James Hinson
# OSU Email: hinsonj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2
# Due Date: 2/5/2024
# Description: Impliments an Abstract Data Type (ADT) Bag.
#              This bag is able to add, remove, count, compare, and clear values,
#              and provides an iterator for navigating through the bag.


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds a new element to the bag.
        
        Args:
            value (object): The value to be added.
        """
        self._da.append(value)


    def remove(self, value: object) -> bool:
        """
        Removes any one element from the bag that matches the provided value object.

        Args:
            value (object): The value to be removed.

        Returns:
            bool: True if some object was actually removed from the bag, otherwise False.
        """
        index = self._find(value)
        if index is not None:
            self._da.remove_at_index(index)
            return True
        return False


    def count(self, value: object) -> int:
        """
        Returns the number of elements in the bag that match the provided value object.

        Args:
            value (object): The value to be counted.

        Returns:
            int: The count of occurrences of the value.
        """
        count = 0
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                count += 1
        return count


    def clear(self) -> None:
        """
        Clears the contents of the bag.
        """
        self._da = DynamicArray()


    def equal(self, second_bag: "Bag") -> bool:
        """
        Compares the contents of a bag with the contents of a second bag.

        Args:
            second_bag (Bag): The second bag to compare with.

        Returns:
            bool: True if the bags are equal, otherwise False.
        """
        if self._da.length() != second_bag._da.length():
            return False

        for i in range(self._da.length()):

            if self.count(self._da.get_at_index(i)) != second_bag.count(self._da.get_at_index(i)):
                return False

        return True


    def __iter__(self):
        """
        Returns an iterator for the bag.
        """
        # Initialize any variables necessary for the iterator
        self._iter_index = 0

        # Return self as the iterator
        return self


    def __next__(self):
        """
        Returns the next element in the bag.
        """
        if self._iter_index < self.size():
            value = self._da.get_at_index(self._iter_index)
            self._iter_index += 1
            return value
        else:
            raise StopIteration


    def _find(self, value: object) -> int:
        """
        Finds the index of the first occurrence of the value in the bag.
        
        Args:
            value (object): The value to find.
        
        Returns:
            int: The index of the value if found, otherwise None.
        """
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                return i

        return None

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
