# Name: James Hinson
# OSU Email: hinsonj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 4
# Due Date: 2/26/24
# Description: Assignment 4 - Binary Search Tree Implementation


import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value   # to store node's data
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Override string method; display in pre-order
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.

        This is intended to be a troubleshooting method to help find any
        inconsistencies in the tree after the add() or remove() operations.
        A return of True from this method doesn't guarantee that your tree
        is the 'correct' result, just that it satisfies bst ordering.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Adds left and right nodes to the tree
        """
        if self._root is None:
            self._root = BSTNode(value)
        else:
            self._add_recursive(self._root, value)


    def _add_recursive(self, node: BSTNode, value: object) -> None:
        """
        Helper method to recursively add a value to the tree.
        """
        if value <= node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._add_recursive(node.right, value)


    def remove(self, value: object) -> bool:
        """
        Removes a value from the tree. Returns True if the value is removed, False otherwise.
        """
        if self._root is None:
            return False  # Tree is empty

        # Initialize parent and current pointers
        parent = None
        current = self._root

        # Search for the node to be removed
        while current:
            if value < current.value:
                parent = current
                current = current.left

            elif value > current.value:
                parent = current
                current = current.right

            else:  # Value found
                # Call appropriate removal function based on the scenario
                if current.left is None and current.right is None:
                    self._remove_no_subtrees(parent, current)
                elif current.left is None or current.right is None:
                    self._remove_one_subtree(parent, current)
                else:
                    self._remove_two_subtrees(parent, current)

                return True

        return False  # Value not found


    def _remove_no_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Removes a node that has no subtrees (no left or right nodes).
        """
        if remove_parent is None:
            self._root = None
        elif remove_parent.left == remove_node:
            remove_parent.left = None
        else:
            remove_parent.right = None


    def _remove_one_subtree(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Removes a node that has a left or right subtree (only).
        """
        if remove_node.left:
            child = remove_node.left
        else:
            child = remove_node.right

        if remove_parent is None:
            self._root = child
        elif remove_parent.left == remove_node:
            remove_parent.left = child
        else:
            remove_parent.right = child


    def _remove_two_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Removes a node that has two subtrees.
        """
        successor_parent = remove_node
        successor = remove_node.right
        while successor.left:
            successor_parent = successor
            successor = successor.left

        # Replace current node with its successor
        remove_node.value = successor.value

        # Remove successor node (it has at most one child)
        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right


    def contains(self, value: object) -> bool:
        """
        Checks if the value is in the tree. Returns True if found, False otherwise.
        """
        return self._contains_recursive(self._root, value)

    def _contains_recursive(self, node: BSTNode, value: object) -> bool:
        """
        Helper method to recursively search for a value in the tree.
        """
        if node is None:
            return False

        if node.value == value:
            return True

        # Recursively search in the left and right subtrees
        return self._contains_recursive(node.left, value) or self._contains_recursive(node.right, value)


    def inorder_traversal(self) -> Queue:
        """
        Performs an inorder traversal of the tree, returning a Queue object
        containing the values of the visited nodes, in the order they were visited.
        If the tree is empty, an empty Queue is returned.
        """
        # Initialize an empty Queue to store the traversal result
        result_queue = Queue()
        
        # If the tree is empty, return the empty Queue
        if self.is_empty():
            return result_queue

        # Initialize an empty stack for iterative inorder traversal
        stack = Stack()
        current = self._root

        # Perform inorder traversal
        while current or not stack.is_empty():
            # Traverse to the leftmost node of the current subtree
            while current:
                stack.push(current)
                current = current.left

            # Visit the top node in the stack
            current = stack.pop()
            # Add the value of the visited node to the result Queue
            result_queue.enqueue(current.value)

            # Traverse to the right subtree
            current = current.right

        # Return the Queue containing inorder traversal result
        return result_queue


    def find_min(self) -> object:
        """
        Returns the minimum value in the tree.
        """
        if not self._root:
            return None
        
        current = self._root
        while current.left:
            current = current.left

        return current.value


    def find_max(self) -> object:
        """
        Returns the maximum value in the tree.
        """
        if not self._root:
            return None
        
        current = self._root
        while current.right:
            current = current.right

        return current.value


    def is_empty(self) -> bool:
        """
        Returns True if the tree is empty, and False otherwise.
        """
        return self._root is None


    def make_empty(self) -> None:
        """
        This method removes all of the nodes from the tree.
        """
        self._root = None


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
