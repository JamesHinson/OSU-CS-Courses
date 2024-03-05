# Name: James Hinson
# OSU Email: hinsonj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 5
# Due Date: 3/4/2024
# Description: Assignment 5 - MinHeap Implementation


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    # -----------------------------------------------------------------------

    def add(self, node: object) -> None:
        """
        Adds a new node to the MinHeap.

        :param node: The node to add to the heap.
        """
        self._heap.append(node)
        self._percolate_up(self._heap.length() - 1)


    def is_empty(self) -> bool:
        """
        Checks if the MinHeap is empty.

        :return: True if the heap is empty, False otherwise.
        """
        return self._heap.is_empty()


    def get_min(self) -> object:
        """
        Returns the minimum value in the MinHeap without removing it.

        :return: The minimum value in the heap.
        :raises MinHeapException: If the heap is empty.
        """
        if self.is_empty():
            raise MinHeapException("Heap is empty")
        return self._heap[0]


    def remove_min(self) -> object:
        """
        Removes and returns the minimum value in the MinHeap.

        :return: The minimum value in the heap.
        :raises MinHeapException: If the heap is empty.
        """
        if self.is_empty():
            raise MinHeapException("Heap is empty")

        min_value = self._heap[0]
        last_index = self._heap.length() - 1

        # Swap the root element with the last element in the heap
        self._heap._swap_elements(0, last_index)

        # Remove the last element from the heap.
        self._heap.remove_at_index(last_index)

        # Ensure heap property is maintained
        if not self.is_empty():
            self._percolate_down(0)

        return min_value


    def build_heap(self, da: DynamicArray) -> None:
        """
        Builds a MinHeap from the elements in the given DynamicArray.
        """
        # Clear the existing heap
        self._heap = DynamicArray()

        # Copy elements from the DynamicArray to the heap
        for i in range(da.length()):
            self._heap.append(da.get_at_index(i))

        # Ensure heap property is maintained
        for i in range(da.length() // 2 - 1, -1, -1):
            self._percolate_down(i)


    def size(self) -> int:
        """
        Returns the number of elements in the MinHeap.

        :return: The number of elements in the heap.
        """
        return self._heap.length()


    def clear(self) -> None:
        """Clears the MinHeap."""
        self._heap = DynamicArray()


    def _percolate_up(self, child_index):
        """
        Performs the percolate up operation to maintain the MinHeap property.
        
        :param child_index: The index of the child node.
        :return: None
        """
        if child_index <= 0:
            return

        parent_index = (child_index - 1) // 2

        # Continue swapping elements upward until the child is greater than or equal to its parent
        while child_index > 0 and self._heap[child_index] < self._heap[parent_index]:
            # Swap the child with its parent
            self._swap_elements(child_index, parent_index)
            # Update indices for the child and its parent
            child_index = parent_index
            parent_index = (child_index - 1) // 2


    def _percolate_down(self, parent_index: int) -> None:
        """
        Performs the percolate down operation to maintain the MinHeap property.
        
        :param parent_index: The index of the parent node.
        :return: None
        """
        # Calculate the indices of the left and right children of the parent node
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2
        
        # Initialize the min_index with the parent index
        min_index = parent_index

        # Compare the value of the left child with the parent node
        if left_child_index < self._heap.length() and self._heap[left_child_index] < self._heap[min_index]:
            min_index = left_child_index
            
        # Compare the value of the right child with the current minimum
        if right_child_index < self._heap.length() and self._heap[right_child_index] < self._heap[min_index]:
            min_index = right_child_index

        # If the minimum index has changed, swap the parent node with the minimum and continue percolating down
        if min_index != parent_index:
            self._swap_elements(parent_index, min_index)
            self._percolate_down(min_index)


    def _swap_elements(self, index1: int, index2: int) -> None:
        """
        Swaps the elements at the specified indices in the underlying DynamicArray.
        
        :param index1: The index of the first element to swap.
        :param index2: The index of the second element to swap.
        :return: None
        """
        temp = self._heap[index1]
        self._heap[index1] = self._heap[index2]
        self._heap[index2] = temp


def heapsort(da: DynamicArray) -> None:
    """
    Sorts the elements of the given DynamicArray in non-decreasing order using the heapsort algorithm.

    :param da: The DynamicArray to be sorted.
    :return: None
    """
    heap = MinHeap()

    heap.build_heap(da)

    for i in range(da.length() - 1, -1, -1):
        da.set_at_index(i, heap.remove_min())


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
