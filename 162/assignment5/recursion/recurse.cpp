/******************************************************
** Program: recurse.cpp
** Author: James Hinson
** Date: 12/7/2023
** Description: The primary program file for the ways_to_top
**				recursion exercise. Acts as the "main" file.
**
** Input: User input for the total number of steps, and
**		  whether or not to run the program again.
**
** Output: The primary loop through which the program runs.
**		   Displays the number of possible unique ways
**		   to get to the top of a staircase of 'n' stairs.
******************************************************/ 

// The following is an example program that
// does some basic, limited testing of your
// ways_to_top() implementation.

#include <iostream>

#include "stairs.h"

using namespace std;

/*********************************************************************
** Function: main
** Description: The main function. Runs the program loop, asking the
**				user for an integer input of num_steps and if they
**				would like to run the program again after completion.
**
** Parameters: num_steps, running, input
** Pre-Conditions: No pre-conditions (called automatically).
** Post-Conditions: The number of possible unique ways to get to the
**					top of a staircase of 'n' stairs is displayed.
*********************************************************************/
int main() {

	int num_steps = 0;
	bool running = true;
	char input;

	cout << "\nDefault examples for calculating ways to top:" << endl;

	cout << "For 3 steps on a staircase, there are " << ways_to_top(3) << " ways to the top." << endl; // Should print 4
	cout << "For 4 steps on a staircase, there are " << ways_to_top(4) << " ways to the top." << endl; // Should print 7
	cout << "For 5 steps on a staircase, there are " << ways_to_top(5) << " ways to the top." << endl; // Should print 13

	cout << "\nPlease enter the number of steps to calculate: ";
	cin >> num_steps;
	cout << "\nFor " << num_steps << " steps on a staircase, there are " << ways_to_top(num_steps) << " ways to the top." << endl;

	/*
		Simple while loop to ask the user if they would like to re-run the program,
		getting a new input and re-running the ways_to_top(num_steps) function if yes.

		Does not contain anything other than simple input validation as this feature
		isn't required, and is for testing purposes & user convenience.
	*/

	while(running) {

		cout << "Would you like to run it again? Y/n: ";
		cin >> input;

		if (input == 'Y' || input == 'y') {

			cout << "\nPlease enter the number of steps to calculate: ";
			cin >> num_steps;
			cout << "\nFor " << num_steps << " steps on a staircase, there are " << ways_to_top(num_steps) << " ways to the top." << endl;

		} else if (input == 'N' || input == 'n') {
			running = false;
		}
	}

	return 0;
}
