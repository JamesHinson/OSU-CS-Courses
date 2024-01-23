/******************************************************
** Program: linked_list.cpp
** Author: James Hinson
** Date: 12/10/2023
** Description: Implementation file for a linked list data structure.
**              Defines methods to manipulate a linked list such as
**              insertion, deletion, sorting, and traversal.
**
** Input: Various inputs depending on the functions:
**        - Data values to be inserted into the linked list
**        - Indices for deletion or insertion
**        - Conditions for sorting functions
**        - User commands or prompts for manipulating the list
**
** Output: Resultant linked list after manipulation:
**         - Displaying the list after insertion/deletion
**         - Displaying sorted lists in ascending or descending order
**         - Error messages or prompts related to the list operations
******************************************************/


#include "linked_list.h"



/*********************************************************************
** Function: Linked_List()
** Description: Constructor for initializing a linked list object.
**
** Parameters: head
**
** Pre-Conditions: None
**
** Post-Conditions: A linked list object is created with a null head.
*********************************************************************/
Linked_List::Linked_List() {
	head = nullptr; // Initialize the head pointer to nullptr
}



/*********************************************************************
** Function: get_length()
** Description: Obtains the length of a linked list.
**
** Parameters: length, current, head
**
** Pre-Conditions: A linked list must be created.
**
** Post-Conditions: Returns the integer length of the linked list.
*********************************************************************/
int Linked_List::get_length() {	
	int length = 0; // Initialize length to zero

	// Traverse the list and count the number of nodes
	Node* current = head;

	while (current != nullptr) {
		length++;
		current = current->next;
	}

	return length;
}



/*********************************************************************
** Function: print()
** Description: Displays the elements in the linked list.
**
** Parameters: current, head
**
** Pre-Conditions: A linked list must be created.
**
** Post-Conditions: The contents of the linked list are printed.
*********************************************************************/
void Linked_List::print() {
	Node* current = head;

	while (current != nullptr) {
		cout << current->val << " ";
		current = current->next;
	}
	
	cout << endl;
	return;
}



/*********************************************************************
** Function: clear()
** Description: Removes all elements in a linked list.
**
** Parameters: current, head, nextNode, length
**
** Pre-Conditions: A linked list must be created.
**
** Post-Conditions: The contents of the linked list are deleted.
*********************************************************************/
void Linked_List::clear() {
	// Delete the entire list (remove all nodes and reset length to 0)
	
	Node* current = head;
	Node* nextNode;

	while (current != nullptr) {
		nextNode = current->next;
		delete current; // Delete the current node
		current = nextNode;
	}

	head = nullptr; // Set the head pointer to null
	length = 0; // Reset the length to 0
	return;
}



/*********************************************************************
** Function: push_front()
** Description: Inserts a new value at the front of a list.
**
** Parameters: val, newNode, head, length
**
** Pre-Conditions: A linked list must be created & an integer value
**				   must be provided.
**
** Post-Conditions: A new value is inserted at the front of the list
**					and the length of the list is updated.
*********************************************************************/
void Linked_List::push_front(int val) {
	// Insert a new value at the front of the list 
	
	Node* newNode = new Node(); // Create a new node
	newNode->val = val; // Set the value for the new node
	newNode->next = head; // Point the new node to the current head

	head = newNode; // Update the head to the new node
	length++; // Increment the length of the list
	return;
}



/*********************************************************************
** Function: push_back()
** Description: Inserts a new value at the back of a list.
**
** Parameters: val, newNode, head, length
**
** Pre-Conditions: A linked list must be created & an integer value
**				   must be provided.
**
** Post-Conditions: A new value is inserted at the end of the list
**					and the length of the list is updated.
*********************************************************************/
void Linked_List::push_back(int val) {
	// Insert a new value at the back of the list
	
	Node* newNode = new Node(); // Create a new node
	newNode->val = val; // Set the value for the new node
	newNode->next = nullptr; // The new node will be the last, so its next should point to null

	if (head == nullptr) {
		head = newNode; // If the list is empty, set the new node as the head
	} else {
		Node* current = head;
		while (current->next != nullptr) {
			current = current->next; // Traverse the list to find the last node
		}
		current->next = newNode; // Set the last node's next to the new node
	}

	length++; // Increment the length of the list
	return;
}



/*********************************************************************
** Function: insert()
** Description: Inserts a new value at a specific index in the list.
**
** Parameters: val, index, newNode, head, currentIndex, length
**
** Pre-Conditions: A linked list must be created & integer values
**				   must be provided.
**
** Post-Conditions: A new value is inserted at the specified index of
**					the list and the length of the list is updated.
*********************************************************************/
void Linked_List::insert(int val, int index) {
	// Insert a new value in the list at the specified index 
	
	if (index < 0 || index > get_length()) {
		// Invalid index, do nothing
		cout << "\nInvalid index for insertion.\n" << endl;
		return;
	}

	if (index == 0) {
		// Insert at the front (same as push_front)
		push_front(val);
	} else if (index == get_length()) {
		// Insert at the back (same as push_back)
		push_back(val);
	} else {
		// Insert at a specific index
		Node* newNode = new Node(); // Create a new node
		newNode->val = val; // Set the value for the new node

		Node* current = head;
		int currentIndex = 0;

		while (currentIndex < index - 1) {
			current = current->next;
			currentIndex++;
		}

		newNode->next = current->next; // Set the new node's next to the node at the current index
		current->next = newNode; // Set the node at the current index's next to the new node

		length++; // Increment the length of the list
	}
	return;
}



/*********************************************************************
** Function: pop_back()
** Description: Removes a new value at the back of a list.
**
** Parameters: val, newNode, head, length
**
** Pre-Conditions: A linked list must be created.
**
** Post-Conditions: A new value is removed at the end of the list
**					and the length of the list is updated.
*********************************************************************/
void Linked_List::pop_back() {
	// Remove the node at the back of the list
	
	if (head == nullptr) {
		// List is empty, handle accordingly (e.g., print an error or return)
		cout << "\nList is empty. Cannot perform pop_back().\n" << endl;
		return;
	}

	Node* current = head;
	Node* prev = nullptr;

	while (current->next != nullptr) {
		prev = current;
		current = current->next;
	}

	// At this point, 'current' is the last node, 'prev' is its predecessor
	if (prev != nullptr) {
		prev->next = nullptr; // Set the previous node's next to null, indicating it's now the last node
	} else {
		// Only one node in the list
		head = nullptr;
	}

	delete current; // Free the memory of the last node
}



/*********************************************************************
** Function: pop_front()
** Description: Removes a new value at the front of a list.
**
** Parameters: temp, head, length
**
** Pre-Conditions: A linked list must be created.
**
** Post-Conditions: A new value is removed at the start of the list
**					and the length of the list is updated.
*********************************************************************/
void Linked_List::pop_front() {
	// Remove the node at the front of the list
	
	if (head == nullptr) {
		// If the list is empty, do nothing
		cout << "\nList is empty. Cannot perform pop_front().\n" << endl;
		return;
	} else {
		Node* temp = head; // Store the current head in a temporary pointer
		head = head->next; // Update the head to the next node
		delete temp; // Delete the old head
		length--; // Decrement the length of the list
	}
	return;
}



/*********************************************************************
** Function: remove()
** Description: Removes a value at a specific index in a list.
**
** Parameters: index, current, head, currentIndex, length
**
** Pre-Conditions: A linked list must be created & an integer value
**				   must be provided.
**
** Post-Conditions: A value is removed at the specified index of
**					the list and the length of the list is updated.
*********************************************************************/
void Linked_List::remove(int index) {
	// Remove the node at index of the list
	
	if (index < 0 || index >= get_length() || head == nullptr) {
		// Invalid index or empty list, do nothing
		cout << "\nInvalid index for removal or list is empty.\n\n";
		return;
	}

	if (index == 0) {
		// If removing the first node, use pop_front()
		pop_front();
	} else {
		Node* current = head;
		Node* prev = nullptr;
		int currentIndex = 0;

		// Traverse the list to reach the node at the specified index
		while (currentIndex < index) {
			prev = current;
			current = current->next;
			currentIndex++;
		}

		prev->next = current->next; // Adjust the pointers to remove the node
		delete current; // Delete the node at the specified index
		length--; // Decrement the length of the list
	}
	return;
}



/*********************************************************************
** Function: sort_ascending()
** Description: Sorts the list ascending by using a merge sort algorithm.
**
** Parameters: head
**
** Pre-Conditions: A linked list must be created.
**
** Post-Conditions: A linked list is sorted by ascending order.
*********************************************************************/
void Linked_List::sort_ascending() {
	// Sort the nodes in ascending order. You must implement the recursive Merge Sort algorithm.

	if (head == nullptr || head->next == nullptr) {
		// If the list is empty or has only one node, it's already sorted
		return;
	}

	head = merge_sort(head);
	return;
}



/*********************************************************************
** Function: merge_sort()
** Description: Contains the logic behind the merge sort algorithm;
**				actually does the recursive sorting of the list. 
**
** Parameters: head, fast, slow, mid, left, right
**
** Pre-Conditions: A linked list must be created & provided as input.
**
** Post-Conditions: A linked list is sorted by ascending order and
**					is returned.
*********************************************************************/
Node* Linked_List::merge_sort(Node* head) {
	// Base case: if list is empty or has only one node, return head
	if (head == nullptr || head->next == nullptr) {
		return head;
	}

	// Find the middle of the list
	Node* slow = head; // Increments only one node at a time (slow)
	Node* fast = head->next; // Increments two nodes at a time (fast)

	while (fast != nullptr && fast->next != nullptr) {
		slow = slow->next;
		fast = fast->next->next;
	}

	Node* mid = slow->next;
	slow->next = nullptr; // Split the list into two halves

	// Recursively sort and merge the two halves
	Node* left = merge_sort(head);
	Node* right = merge_sort(mid);

	return merge(left, right); // Merge the sorted halves and return the sorted list
}



/*********************************************************************
** Function: merge()
** Description: Recursively merges two halves of a list, returning 
**				the result as one list.
**
** Parameters: left, right, result
**
** Pre-Conditions: A linked list must be created & two sub-lists must be
**				   provided as inputs.
**
** Post-Conditions: A new list is created by merging two smaller lists
**					and is returned.
*********************************************************************/
Node* Linked_List::merge(Node* left, Node* right) {
	Node* result = nullptr;

	// If left or right is null, return the other (already sorted)
	if (left == nullptr) {
		return right;
	} else if (right == nullptr) {
		return left;
	}

	// Merge the two lists based on node values
	if (left->val <= right->val) {
		result = left;
		result->next = merge(left->next, right); // Recursively merge the remaining nodes
	} else {
		result = right;
		result->next = merge(left, right->next); // Recursively merge the remaining nodes
	}

	return result; // Return the merged list
}



/*********************************************************************
** Function: sort_descending()
** Description: Sorts the list descending by using a selection sort
**				algorithm.
**
** Parameters: head
**
** Pre-Conditions: A linked list must be created.
**
** Post-Conditions: A linked list is sorted by descending order.
*********************************************************************/
void Linked_List::sort_descending() {
	// sort the nodes in descending order using the Selection Sort algorithm
	
	head = selection_sort(head);
	return;
}



/*********************************************************************
** Function: find_min()
** Description: Finds the minimum integer value in a provided list.
**
** Parameters: head, minNode, current
**
** Pre-Conditions: A linked list must be created & provided as input.
**
** Post-Conditions: A minimum value is returned after being found.
*********************************************************************/
Node* Linked_List::find_min(Node* head) {
	Node* minNode = head;
	Node* current = head->next;

	// Traverse the list to find the minimum node
	while (current != nullptr) {
		if (current->val < minNode->val) {
			minNode = current;
		}
		current = current->next;
	}

	return minNode; // Return the node with the minimum value
}



/*********************************************************************
** Function: selection_sort()
** Description: Contains the logic behind the selection sort algorithm;
**				actually does the iterative sorting of the list. 
**
** Parameters: head, prev, minNode, sortedList
**
** Pre-Conditions: A linked list must be created & a linked list
**				   must be provided.
**
** Post-Conditions: A linked list is sorted by descending order and
**					returned.
*********************************************************************/
Node* Linked_List::selection_sort(Node* head) {
	Node* sortedList = nullptr; // Initialize the sorted list

	while (head != nullptr) { // Continue until the original list is empty
		Node* minNode = find_min(head); // Find the node with the minimum value in the unsorted part of the list

		if (minNode == head) { // If the minimum node is the current head
			head = head->next; // Move the head to the next node
		} else {
			Node* prev = head;
			while (prev->next != minNode) { // Find the node before the minimum node
				prev = prev->next;
			}
			prev->next = minNode->next; // Remove the minimum node from its current position
		}

		minNode->next = sortedList; // Add the minimum node to the sorted list
		sortedList = minNode;
	}

	return sortedList; // Return the head of the sorted list
}
