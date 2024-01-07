
Note to TA: There is a separate readme.txt file for Part 1 (recursive stairs) in the "recursion" folder
for ease of readability. I checked with Alex to make sure I was allowed to have separate readme files.
Also if Bruce Yan is grading this, then hello and thank you for your time!

1. Name and Student ID #:

	James Hinson (934-430-054)


2. Description: One paragraph advertising what your program does (for a user who knows
nothing about this assignment, does not know C++, and is not going to read your code).
Highlight any special features.

	This program is designed to manage a linked list data structure. A linked list is a linear
	collection of elements where each element points to the next one in the sequence, creating a
	"linked" line of elements. The program provides functionalities to manipulate this linked list,
	including the insertion, deletion, sorting, and traversal of list elements. It offers an intuitive
	interface for users to add, remove, and sort elements in the list. Its special feature includes
	implementing a selection sort algorithm to arrange the elements either in ascending or descending
	order.


3. Instructions: Step-by-step instructions telling the user how to compile and run your
program. Each menu choice should be described. If you expect a certain kind of input at
specific steps, inform the user what the requirements are. Include examples to guide the
user.

	Compilation and Execution:

		Compilation: Use a C++ compiler like g++ with the command

		g++ -std=c++11 linked_list.cpp -o linked_list 

		or simply type 'make' in a terminal while in the folder containing the .cpp, .h, and 'makefile'
		files, which will compile the program for you assuming the 'make' utility is installed.

		Execution: Run the program by executing ./linked_list in the terminal.

	Program Menu:

		The program provides the following options, demonstrated by test cases when you run the program:

			Add Node: Allows users to add elements to the linked list.
			Remove Node: Enables the removal of elements from the linked list.
			Sort Ascending: Sorts the elements in ascending order using a merge sort algorithm.
			Sort Descending: Sorts the elements in descending order using a selection sort algorithm.
			Display List: Shows the current elements present in the linked list.
			Exit: Terminates the program.

		Input Requirements:

			For adding nodes: Enter integer values to be inserted into the linked list.
			For removing nodes: Specify the index of the element to remove.

			For sorting:
			
				Sort Ascending: Uses the merge sort algorithm to arrange elements in ascending order.
					
				Sort Descending: Uses the selection sort algorithm to arrange elements in descending
				order.


4. Limitations: Describe any known limitations for things the user might want or try to do
but that program does not do/handle.

	Limited to handling integer data types.
	Not equipped for complex operations or data manipulations beyond basic linked list functionalities.
	May not efficiently handle very large datasets due to the selection sort algorithm's complexity.


5. (Part 2 only) Extra credit: If your program includes extra credit work, describe it here for
the user.

	The program includes an implementation of the selection sort algorithm for sorting elements in
	descending orders, which can be seen in the selection_sort() function called by sort_descending().


6. (Part 2 only) Complexity analysis: For each of the following function, explain the
algorithm you used and the Big O for runtime complexity

	a. sort_ascending()

		Algorithm Used: Merge Sort
		Runtime Complexity (Big O): O(n log(n))

		Description:
			Merge sort works by dividing an unsorted list into smaller sub-lists, sorting each sub-list
			recursively (by ascending order in this case), and finally merging them back together to
			create a sorted list.

	b. sort_descending()

		Algorithm Used: Selection Sort
		Runtime Complexity (Big O): O(n^2)

		Description:
			Selection sort works by repeatedly selecting the smallest element from an unsorted portion
			of a list and placing it at the beginning of the sorted portion. It involves scanning the
			list to find the smallest element and swapping it with the first unsorted element. This
			process continues iteratively, with each iteration reducing the size of the unsorted portion
			by one element. This continues until the full list is sorted.
