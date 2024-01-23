/******************************************************
** Program: main.cpp
** Author: James Hinson
** Date: 11/26/2023
** Description: The main program file for the Hunt the Wumpus game 
** Input: User input for the dimensions of the map, whether or not debug mode
** 		  is active
** Output: The gameplay loop through the play_game function
******************************************************/ 

#include <iostream>
#include <cstdlib>
#include <ctime>
#include "game.h"

using namespace std;


int main() {
	// set the random seed
	srand(time(NULL));
	
	int wid = 0, len = 0;
	bool debug = false;
	string debug_input;

	cout << "Welcome to Hunt the Wumpus!" << endl;

	Game g;

	// get two inputs: size of the cave (wid and len)
	// also checks that the inputs are valid for width and length
	
	len = g.get_dimension("rows");
	wid = g.get_dimension("columns");

	// get the 3rd input --> debug mode or not
	cout << endl;
	cout << "Would you like to play in debug mode? Y/n: ";
	cin >> debug_input;

	debug = g.is_debug(debug_input);

	cout << "\nAbout to start the game..!\n" << endl;

	// Play game - length, width, debug mode, new game or not
	g.play_game(len, wid, debug, true);

	return 0;
}
