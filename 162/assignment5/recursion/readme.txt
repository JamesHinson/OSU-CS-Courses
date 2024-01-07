
Note to TA: This is the separate readme.txt file for Part 1 (recursive stairs). The readme for Part 2
can be found in the folder/directory containing the "recursion" and "linked_list" sub directories. I
checked with Alex to make sure I was allowed to have separate readme files. Also if Bruce Yan is grading
this, then hello and thank you for your time!

1. Name and Student ID #:

	James Hinson (934-430-054)


2. Description: One paragraph advertising what your program does (for a user who knows
nothing about this assignment, does not know C++, and is not going to read your code).
Highlight any special features.

	This program calculates the number of unique ways to climb a staircase with a specified number of
	steps using steps of sizes 1, 2, or 3. It uses a recursive algorithm to determine the various
	combinations of steps that lead to the top of the staircase. The special feature of this program
	lies in its ability to compute the total distinct ways to climb the stairs while considering step
	sizes, providing the user with the total unique solutions for a given number of steps.


3. Instructions: Step-by-step instructions telling the user how to compile and run your
program. Each menu choice should be described. If you expect a certain kind of input at
specific steps, inform the user what the requirements are. Include examples to guide the
user.

	Compilation and Execution:

		Compilation: Use a C++ compiler like g++ with the command 

		g++ -std=c++11 recurse.cpp stairs.cpp -o stairs

		or simply type 'make' in a terminal while in the folder containing the .cpp, .h, and 'makefile'
		files, which will compile the program for you assuming the 'make' utility is installed.

		Execution: 

			Running the Program:
				Run the program by executing ./stairs in the terminal.

				Upon execution, the program will display default examples of staircases with 3, 4, and 5
				steps and their respective ways to the top.

				Then, the program prompts the user to input the number of steps for which they want to
				calculate the unique ways to get to the top.

				Enter a non-negative integer to determine the number of steps in the staircase.

				The program will then display the number of unique ways to climb the staircase.

				Additionally, the program will ask if the user wants to run it again; provide 'Y' or 'N'
				as input accordingly.


4. Limitations: Describe any known limitations for things the user might want or try to do
but that program does not do/handle.

	Large inputs might lead to longer processing times or could potentially cause the program to exceed
	recursion depth due to the nature of recursive computation, leading to a stack overflow error.

	The program does not handle non-integer inputs or floating-point numbers for the number of steps.
	Therefore, it requires an integer input, and decimals or fractions are not supported for this input
	field.