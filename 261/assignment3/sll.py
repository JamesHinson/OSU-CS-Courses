# Name: James Hinson
# OSU Email: hinsonj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: 2/12/2024
# Description: A custom Singly Linked List that contains many features.
#              Includes support for traversing a list, inserting & removing at indicies,
#              counting and finding value occurences, and slicing list values.

from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Inserts a new node with the given value at the front of the linked list.
        """
        new_node = SLNode(value)
        new_node.next = self._head.next
        self._head.next = new_node


    def insert_back(self, value: object) -> None:
        """
        Inserts a new node with the given value at the back of the linked list.
        """
        new_node = SLNode(value)
        current = self._head

        while current.next:
            current = current.next

        current.next = new_node


    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a new node with the given value at the specified index in the linked list.
        """
        if index < 0:
            raise SLLException("Invalid index")

        new_node = SLNode(value)

        current = self._head

        # Traverse the linked list to find the node at the specified index
        for _ in range(index):
            if current.next is None:
                raise SLLException("Index out of range")
            current = current.next

        # Connect the new node to the next node after the current node
        new_node.next = current.next

        # Connect the current node to the new node
        current.next = new_node


    def remove_at_index(self, index: int) -> None:
        """
        Removes the node at the specified index in the linked list.
        """
        if index < 0:
            raise SLLException("Invalid index")

        current = self._head

        # Traverse the linked list to find the node at the specified index
        for _ in range(index):
            if current.next is None:
                raise SLLException("Index out of range")
            current = current.next

        # Check and raise exception if the next node is out of range
        if current.next is None:
            raise SLLException("Index out of range")

        # Remove the next node of the current node by skipping over it
        current.next = current.next.next


    def remove(self, value: object) -> bool:
        """
        Removes the first occurrence of the node with the given value from the linked list.
        """
        current = self._head

        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return True

            current = current.next

        return False


    def count(self, value: object) -> int:
        """
        Counts the number of occurrences of the given value in the linked list.
        """
        count = 0
        current = self._head.next

        while current:
            if current.value == value:
                count += 1
            current = current.next

        return count


    def find(self, value: object) -> bool:
        """
        Determines whether the given value exists in the linked list.
        """
        current = self._head.next

        while current:
            if current.value == value:
                return True
            current = current.next

        return False


    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        Returns a new linked list that contains a slice of the original list starting from
        the specified index with the specified size.
        """
        # Validate start_index and size
        if start_index < 0:
            raise SLLException("Invalid start index")
        if size < 0:
            raise SLLException("Invalid size")

        # Traverse to the start_index
        current = self._head.next
        
        for _ in range(start_index):
            if current is None:
                raise SLLException("Start index out of range")

            current = current.next

        # Check if start_index is out of range
        if current is None:
            raise SLLException("Start index out of range")

        # Calculate the actual size of the remaining elements
        actual_size = 0

        while current is not None:
            actual_size += 1
            current = current.next

        # Check if the requested slice size exceeds the available elements
        if size > actual_size:
            raise SLLException("Size exceeds available elements in the list")

        # Reset current to the start_index node
        current = self._head.next

        for _ in range(start_index):
            current = current.next

        # Slice the list and create a new LinkedList
        new_list = LinkedList()
        
        for _ in range(size):
            new_list.insert_back(current.value)
            current = current.next

        # Return the sliced LinkedList
        return new_list


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
