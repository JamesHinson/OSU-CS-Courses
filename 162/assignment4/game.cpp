/******************************************************
** Program: game.cpp
** Author: James Hinson
** Date: 11/30/2023
** Description: The game.cpp file for the game. Provides
** 				almost all of the core game logic and loop
** Input: User input to navigate the map & menu, shoot arrows,
** 		  whether or not to play again; if playing again,
**		  whether the user wants the same or a new map, plus
**		  debug mode or not
**
** Output: The map and game status printed to the screen
******************************************************/ 

#include "game.h"
#include "gold.h"
#include "stalactites.h"
#include "bats.h"
#include "wumpus.h"

#include <iostream>

using namespace std;


/*********************************************************************
** Function: Game()
** Description: The game constructor - creates a base game with all values
**				set to their defaults
**
** Parameters: 	map_size
**				player_start_x
**				player_start_y
**				current_position_x
**				current_position_y
**				confused_timer
**				move_choice
**				game_over
**				game_won
**				is_confused
**				carrying_gold
**				gold_at_start
**				wumpus_killed
**
** Pre-Conditions: A game object must be requested
**
** Post-Conditions: A new game object is created with all default values
*********************************************************************/
Game::Game() {
	map_size = 0;
	player_start_x = 0;
	player_start_y = 0;
	current_position_x = 0;
	current_position_y = 0;
	confused_timer = 0;
	move_choice = ' ';
	game_over = false;
	game_won = false;
	is_confused = false;
	carrying_gold = false;
	gold_at_start = false;
	wumpus_killed = false;
}



/*********************************************************************
** Function: ~Game()
** Description: The game destructor; frees memory at the end of the program
**
** Parameters: None
**
** Pre-Conditions: Memory must be allocated
**
** Post-Conditions: Memory is freed
*********************************************************************/
Game::~Game() {
	// Game destructor

	// Realized using the code below was bad practice; omitted but kept to ask TA

	// for (int i = 0; i < this->length; i++) {
	// 	for (int j = 0; j < this->width; j++) {
	// 		this->map[i][j].~Room();
	// 	}
	// }
}



/*********************************************************************
** Function: set_up
** Description: Sets up a new map using 2D vectors, adding all events
** 				and the player to the active game object. 
**
** Parameters: l, w, length, width, num_arrows, 
**			   map_size, player_start_x, player_start_y, 
**			   current_position_x, current_position_y, map, gold_added, 
**			   wumpus_added, found_empty_room, random_room_x, random_room_y
**
** Pre-Conditions: reg_score, money_score, starry_score, and money_rack 
** 				   must have integer values when the function is called.
**
** Post-Conditions: A new 2D vector of Room objects is created for the map,
**					and all rooms are randomly filled with either an event,
**					the player, or no event
*********************************************************************/
void Game::set_up(int l, int w) {
	// Set up the game
	this->length = l; // Number of rows
	this->width = w; // Number of columns

	this->num_arrows = 3; 	// Start with 3 arrows

	// cout << "Length: " << l << endl; // Internal debugging use
	// cout << "Width: " << w << endl; // Internal debugging use
	this->map_size = l * w;

	// cout << "Starting map creation & game setup!" << endl; // Internal debugging use

	// Create the game board: 2D vector of Room objects
	vector<vector<Room>> map(l, vector<Room>(w, Room()));

	for (int i = 0; i < l; i++) {
		for (int j = 0; j < w; j++) {
			map[i][j] = Room();
		}
	}

	// cout << "Created a map with " << this->map_size << " total rooms!\n" << endl; // Internal debugging use

	// randomly insert events (2 bats, 2 stalactites, 1 wumpus, 1 gold)
	// into the game
	player_start_x = set_random_room(l); // random location in all possible rows
	player_start_y = set_random_room(w); // random location in all possible columns

	// cout << "Assigned player a random room, waiting to set it...\n" << endl; // Internal debugging use

	// Sets the starting location for the player & checks that the indices are within bounds
	if (in_bounds(player_start_x, player_start_y)) {

		// Access the Room object and set the player location
		map[player_start_x][player_start_y].set_player('*');

		current_position_x = player_start_x;
		current_position_y = player_start_y;

		// cout << "Set player starting location at (" << player_start_x + 1 << "," << " "<< player_start_y + 1 << ")" << endl;
		// Internal debugging use ^

		int tmp_start_x = (player_start_x + 4) % (w + 1);

		/*
			Note: the code below is technically wrong since you need to flip the x and y values here,
			but the actual dimensions stay the same. This is only to display the player starting position 
			accurately.
		 */

		cout << "Player start: [" << player_start_y + 1 << ", " << tmp_start_x << "]" << endl;
		cout << endl;

	} else {
		std::cout << "Invalid indices for accessing the 2D matrix.\n" << endl;
	}

	// Sets a random valid location for the gold object
	bool gold_added = false;

	int random_room_x = set_random_room(l);
	int random_room_y = set_random_room(w);

	while (!gold_added) {
		if (map[random_room_x][random_room_y].get_player() != '*') {
			map[random_room_x][random_room_y].set_event('$');
			// cout << "Set Gold event!" << endl; // Internal debugging use
			// cout << map[random_room_x][random_room_y].get_percepts(); // Internal debugging use
			gold_added = true;
		} else {
			random_room_x = set_random_room(l);
			random_room_y = set_random_room(w);
		}
	}
	
	// Sets a random valid location for the Wumpus
	bool wumpus_added = false;

	random_room_x = set_random_room(l);
	random_room_y = set_random_room(w);

	while (!wumpus_added) {
		if (map[random_room_x][random_room_y].get_player() != '*') {
			map[random_room_x][random_room_y].set_event('W');
			// cout << "Set Wumpus event!" << endl; // Internal debugging use
			// cout << map[random_room_x][random_room_y].get_percepts(); // Internal debugging use
			wumpus_added = true;
		} else {
			random_room_x = set_random_room(l);
			random_room_y = set_random_room(w);
		}
	}


	bool found_empty_room;

	// Loops through twice, setting a random valid location for the Bats and Stalactite events
	// A valid location is any Room that doesn't already contain an Event or the player
	for (int i = 0; i < 2; i++)
	{
		found_empty_room = false;
		random_room_x = set_random_room(l);
		random_room_y = set_random_room(w);

		// cout << "\nStarting loop " << (i + 1) << " of 2:" << endl; // Internal debugging use
		while (!found_empty_room) {

			if (map[random_room_x][random_room_y].get_event() == ' ' && map[random_room_x][random_room_y].get_player() != '*') {
				map[random_room_x][random_room_y].set_event('B');
				// cout << "Set Bats event " << (i + 1) << "!" << endl; // Internal debugging use
				// cout << map[random_room_x][random_room_y].get_percepts(); // Internal debugging use
				found_empty_room = true;
			} else {
				random_room_x = set_random_room(l);
				random_room_y = set_random_room(w);
			}
		}

		found_empty_room = false;

		random_room_x = set_random_room(l);
		random_room_y = set_random_room(w);

		while (!found_empty_room) {

			if (map[random_room_x][random_room_y].get_event() == ' ' && map[random_room_x][random_room_y].get_player() != '*') {
				map[random_room_x][random_room_y].set_event('V');
				// cout << "Set Stalactites event " << (i + 1) << "!" << endl; // Internal debugging use
				// cout << map[random_room_x][random_room_y].get_percepts(); // Internal debugging use
				found_empty_room = true;
			} else {
				random_room_x = set_random_room(l);
				random_room_y = set_random_room(w);
			}
		}
	}

	// cout << "\nFinished setting events!" << endl; // Internal debugging use

	this->map = map;
}



/*********************************************************************
** Function: display_game
** Description: Prints the map and all percepts, events, and 
**				status updates to the screen
**
** Parameters: line, debug_view, length, width, map[][],
**
** Pre-Conditions: Map must be created and initialized
**
** Post-Conditions: The map and all events/statuses are displayed
*********************************************************************/
void Game::display_game() const {

	cout << "\nArrows remaining: " << this->num_arrows << endl;
	
	string line = "";
	for (int i = 0; i < this->width; i++) {
		line += "-----";
	}

	for (int i = 0; i < this->length; i++)
	{
		cout << line << endl;
		for (int j = 0; j < this->width; j++)
		{
			cout << " ";

			// If the player is in the current room:
			if (map[i][j].get_player() == '*') {
				cout << "* ||";

			} else {
				// If debugging view is true, print out objects in all rooms, otherwise just print " "
				if (debug_view == true) {
					cout << map[i][j].get_event() << " ||";

				} else {
					cout << "  ||";
				}
			}
		}
		cout << endl;
	}
	cout << line << endl;

	//example output (when finished):
	// --------------------
	//  B || G || B ||   ||
	// --------------------
	//    || W ||   || S ||
	// --------------------   
	//    ||   ||   || S ||
	// --------------------   
	// *  ||   ||   ||   ||
	// --------------------
}

/*********************************************************************
** Function: get_dimension
** Description: Gets the dimensions of an individual dimension from the user
**
** Parameters: choice, len
**
** Pre-Conditions: Function must be called
**
** Post-Conditions: An integer is returned, providing the size of the dimension
*********************************************************************/
int Game::get_dimension(string choice) {
	int len = 0;
	do {

		if (cin.fail()) { // Returns 'true' if input is invalid
			cin.clear();
			cin.ignore(1000, '\n'); // Ignores up to 1000 characters of text to take new input
		}

		cout << "\nHow many " << choice << " would you like the map to have? Enter a number between 4 and 50: ";
		cin >> len;
		cout << endl;

	} while (cin.fail() || (len < 4 || len > 50)); // Repeat until a valid integer is entered
	return len;
}



/*********************************************************************
** Function: set_random_room
**
** Description: The input is used to get a random x and y position for whichever is needed
**
** Parameters: input, random_room
**
** Pre-Conditions: Function must be called
**
** Post-Conditions: An integer representing the random room (x or y) is returned
*********************************************************************/
int Game::set_random_room(int input) {
	int random_room = rand() % input;
	// cout << "Randomly selected room number: " << random_room << endl; // Debug purposes
	return random_room;
}



/*********************************************************************
** Function: is_debug
** Description: Checks the user input to determine if the game should
**				be played in debug mode or not
**
** Parameters: debug_input
**
** Pre-Conditions: Function must be called
**
** Post-Conditions: A boolean is returned
*********************************************************************/
bool Game::is_debug(string debug_input) {
	if (debug_input == "y" || debug_input == "Y" || debug_input == "yes" || debug_input == "Yes") {
		return true;
	} else {
		return false;
	}
}



/*********************************************************************
** Function: check_win
** Description: Checks if the user has won the game
**
** Parameters: wumpus_killed, gold_at_start
**
** Pre-Conditions: The necessary parameters must be initalized and valid
**
** Post-Conditions: A boolean is returned
*********************************************************************/
bool Game::check_win() {
	// check if game won
	 if (wumpus_killed == true || gold_at_start == true) {
	 	game_won = true;
		return true;
	} else {
		return false;
	}
}



/*********************************************************************
** Function: check_event
** Description: Checks if there is an event at the player's current
**  			location. Additionally serves as a countdown for the confusion timer
**
** Parameters: confused_timer, is_confused, map[][], current_position_x,
**			   current_position_y, game_over, carrying_gold, gold_at_start
**
** Pre-Conditions: The necessary parameters must be initalized and valid
**
** Post-Conditions: Confusion timer counts down or is activated,
** 					carrying_gold or gold_at_start set to true
*********************************************************************/
void Game::check_event() {

	if (confused_timer == 0) {
		is_confused = false;

	} else {
		cout << "\nConfusion remaining: " << confused_timer << endl;
		confused_timer--;
	}

	if (map[current_position_x][current_position_y].get_event() == 'W') {
		cout << "\nYou encountered the Wumpus and were eaten. Game over!" << endl;
		game_over = true;

	} else if (map[current_position_x][current_position_y].get_event() == 'V') {
		cout << "\nYou were hit by a falling stalactite and died. Game over!" << endl;
		game_over = true;

	} else if (map[current_position_x][current_position_y].get_event() == 'B') {
		cout << "\nYou have encountered Super Bats. You feel confused (Lasts 5 turns)" << endl;
		confused_timer = 4;
		is_confused = true;

	} else if (map[current_position_x][current_position_y].get_event() == '$') {
		cout << "\nYou have found gold, bring it back to the start!" << endl;
		map[current_position_x][current_position_y].set_event(' ');
		carrying_gold = true;

	} else if ((current_position_x == player_start_x && current_position_y == player_start_y) && carrying_gold) {
		gold_at_start = true;
	}
}



/*********************************************************************
** Function: display_percepts
** Description: Displays the percepts adjacent to the player
**
** Parameters: map[][], current_position_x, current_position_y
**
** Pre-Conditions: Map must be created and events added
**
** Post-Conditions: Percepts are displayed to the player
*********************************************************************/
void Game::display_percepts() const {
	// Percept message above the player
	if (current_position_x > 0 && ((map[current_position_x - 1][current_position_y].get_event() == 'W') || 
		(map[current_position_x - 1][current_position_y].get_event() == 'B') || 
		(map[current_position_x - 1][current_position_y].get_event() == 'V') || 
		(map[current_position_x - 1][current_position_y].get_event() == '$'))) 
	{
		cout << map[current_position_x - 1][current_position_y].get_percepts();
	}

	// Percept message below the player
	if (current_position_x > 0 && ((map[current_position_x + 1][current_position_y].get_event() == 'W') || 
		(map[current_position_x + 1][current_position_y].get_event() == 'B') || 
		(map[current_position_x + 1][current_position_y].get_event() == 'V') || 
		(map[current_position_x + 1][current_position_y].get_event() == '$'))) 
	{
		cout << map[current_position_x + 1][current_position_y].get_percepts();
	}

	// Percept message to the right of the player
	if (current_position_x > 0 && ((map[current_position_x][current_position_y - 1].get_event() == 'W') || 
		(map[current_position_x][current_position_y - 1].get_event() == 'B') || 
		(map[current_position_x][current_position_y - 1].get_event() == 'V') || 
		(map[current_position_x][current_position_y - 1].get_event() == '$'))) 
	{
		cout << map[current_position_x][current_position_y - 1].get_percepts();
	}

	// Percept message to the left of the player
	if (current_position_x > 0 && ((map[current_position_x][current_position_y + 1].get_event() == 'W') || 
		(map[current_position_x][current_position_y + 1].get_event() == 'B') || 
		(map[current_position_x][current_position_y + 1].get_event() == 'V') || 
		(map[current_position_x][current_position_y + 1].get_event() == '$'))) 
	{
		cout << map[current_position_x][current_position_y + 1].get_percepts();
	}
}


void Game::move_up() {
	// Move player up if confusion isn't active, otherwise move player down
	if (current_position_x > 0 && !is_confused) {
		// Previous position
		map[current_position_x][current_position_y].set_player(' ');
		current_position_x--;
		map[current_position_x][current_position_y].set_player('*');

	} else if (current_position_x < (length - 1) && is_confused) {
		map[current_position_x][current_position_y].set_player(' ');
		current_position_x++;
		map[current_position_x][current_position_y].set_player('*');

	} else {
		cout << "\n\nThat's out of bounds! Try again" << endl;
	}

	this->map = map;
}

void Game::move_down() {
	// Move player down if confusion isn't active, otherwise move player up
	if (current_position_x < (length - 1) && !is_confused) {
		// Previous position
		map[current_position_x][current_position_y].set_player(' ');
		current_position_x++;
		map[current_position_x][current_position_y].set_player('*');

	} else if (current_position_x > 0 && is_confused) {
		map[current_position_x][current_position_y].set_player(' ');
		current_position_x--;
		map[current_position_x][current_position_y].set_player('*');

	} else {
		cout << "That's out of bounds! Try again" << endl;
	}

	this->map = map;
}

void Game::move_left() {
	// Move player left
	if (current_position_y > 0 && !is_confused) {
		// Previous position
		map[current_position_x][current_position_y].set_player(' ');
		current_position_y--;
		map[current_position_x][current_position_y].set_player('*');

	} else if (current_position_y < (width - 1) && is_confused) {
		map[current_position_x][current_position_y].set_player(' ');
		current_position_y++;
		map[current_position_x][current_position_y].set_player('*');

	} else {
		cout << "That's out of bounds! Try again" << endl;
	}

	this->map = map;	
}

void Game::move_right() {
	// Move player right
	if (current_position_y < (width - 1) && !is_confused) {
		// Previous position
		map[current_position_x][current_position_y].set_player(' ');
		current_position_y++;
		map[current_position_x][current_position_y].set_player('*');

	} else if (current_position_y > 0 && is_confused) {
		map[current_position_x][current_position_y].set_player(' ');
		current_position_y--;
		map[current_position_x][current_position_y].set_player('*');

	} else {
		cout << "That's out of bounds! Try again" << endl;
	}

	this->map = map;
}

char Game::get_dir() {
	// get direction of arrow:
	char dir;
	// Note: error checking is needed!! 
	// Your code here:
	cout << "Fire an arrow...." << endl;
	cout << "W-up" << endl;
	cout << "A-left" << endl;
	cout << "S-down" << endl;
	cout << "D-right" << endl;
	

	cout << "Enter direction: ";
	cin >> dir;
	cin.ignore(256, '\n');

	return dir;
}

void Game::wumpus_move() {
	// after a missed arrow, 75% chance that the wumpus is moved to a different room

	// How to get 75%? 
	// Hint: generate a random number from 0-3, if the number is not 0, then move

	// Your code here:
	cout << "Game::wumpus_move() is not implemented..." << endl;
	
	return;
}

bool Game::in_bounds(int x, int y) {
	if ((x > map_size - 1 || x < 0) || (y > map_size - 1 || y < 0)){
		return false;
	} else {
		return true;
	}
}

void Game::fire_arrow() {
	// The player may fire arrow...
	char dir = get_dir();
	int x, y;


	if (dir == 'w') {
			// Keep moving the arrow until it hits a wall or passes through 3 rooms
				for (int i = 1; i < 4; i++) {
					x = current_position_x + i;
					y = current_position_y;

					if (in_bounds(x, y) && (map[x][y].get_event() == 'w')) {
						cout << "You killed the Wumpus!" << endl;
						wumpus_killed = true;
						break;
					} else { 
						cout << "You didn't kill the Wumpus!" << endl;
				}
			}
		} else if (dir == 'a') {
				// Keep moving the arrow until it hits a wall or passes through 3 rooms
				for (int i = 1; i < 4; i++) {
					x = current_position_x;
					y = current_position_y - 1;
					if (in_bounds(x, y) && (map[x][y].get_event() == 'w')) {
						cout << "You  killed the Wumpus!" << endl;
						wumpus_killed = true;
						break;
					} else { 
						cout << "You didn't kill the Wumpus!" << endl;
				}
			}
		} else if (dir == 'd') {
				// Keep moving the arrow until it hits a wall or passes through 3 rooms
				for (int i = 1; i < 4; i++) {
					x = current_position_x;
					y = current_position_y + 1;
					if (in_bounds(x, y) && (map[x][y].get_event() == 'w')) {
						cout << "You  killed the Wumpus!" << endl;
						wumpus_killed = true;
						break;
					} else { 
						cout << "You didn't kill the Wumpus!" << endl;
				}
			}
		} else if (dir == 's') {
			// Keep moving the arrow until it hits a wall or passes through 3 rooms
			for (int i = 1; i < 4; i++) {
				x = current_position_x + 1;
				y = current_position_y;
				if (in_bounds(x, y) && (map[x][y].get_event() == 'w')) {
					cout << "You killed the Wumpus!" << endl;
					wumpus_killed = true;
					break;
				} else { 
					cout << "You did not kill the Wumpus!" << endl;
			}
		}
	}
}

void Game::move(char c) {
	// Handle player's action: move or fire an arrow
	if (c == 'f'){
		Game::fire_arrow();
		return;
	}

	switch(c) {
		case 'w':
			Game::move_up();
			break;
		case 'a':
			Game::move_left();
			break;
		case 's':
			Game::move_down();
			break;
		case 'd':
			Game::move_right();
			break;
	}
}

char Game::get_input(){
	// get action, move direction or firing an arrow

	// Note: error checking is needed!!
	// Your code here:
	char c;

	cout << endl << endl << "Player move..." << endl << endl;
	cout << "W-up" << endl;
	cout << "A-left" << endl;
	cout << "S-down" << endl;
	cout << "D-right" << endl;
	cout << "f-fire an arrow" << endl;

	cout << "Enter input: ";
	cin >> c;
	cin.ignore(256, '\n');

	
	return c;
}


void Game::start_over() {
	int choice;
	string debug_input;
	bool debug;

	if (game_won == true) {
		cout << "You won the game, congrats!" << endl;
	}
	
	cout << "\nIf you would like to play again, please choose either 1 or 2: " << endl;
	cout << " 1. Start game over with the same cave "<< endl;
	cout << " 2. Start game over with a new random cave" << endl; 
	cout << " 3. Exit game" << endl;
	cout << "\nEnter input: ";
	cin >> choice;
	
	if (choice == 1) {
		map[current_position_x][current_position_y].set_player(' ');
		this->current_position_x = player_start_x;
		this->current_position_y = player_start_y;
		map[current_position_x][current_position_y].set_player('*');
		cout << "Would you like to play in debug mode this time? (Reveals all traps) Y/n: ";
		cin >> debug_input;
		debug = is_debug(debug_input);
		this->game_won = false;
		Game::play_game(length, width, debug, false);

	} else if (choice == 2) {
		int new_length = get_dimension("rows");
		int new_width = get_dimension("columns");
		cout << "Would you like to play in debug mode this time? (Reveals all traps) Y/n: ";
		cin >> debug_input;
		debug = is_debug(debug_input);
		Game::play_game(new_length, new_width, debug, true);

	} else { 
		cout << "Thanks for playing!" << endl;

	}
}


void Game::play_game(int l, int w, bool d, bool new_game) {

	// cout << "Made it to the start of the play_game function!" << endl; // Internal debugging use
	if (new_game == true) {
		// Game::~Game();
		Game::set_up(l, w);
	}

	// cout << "Made it past game setup!" << endl; // Internal debugging use

	this->debug_view = d;

	char input, arrow_input;
	
	// cout << "About to display the map!" << endl; // Internal debugging use

	while (game_won == false && game_over == false) {
		// print game board
		Game::display_game();

		// checks whether the player has won or not
		check_win();
		
		if (game_won) {
			cout << "Congratulations, you won the game!" << endl;
			return;

		} else if (game_over) {
			cout << "Oh no! You lost the game - better luck next time!" << endl;
			return;
		}

		// display percepts around player's location
		display_percepts();

		// Player move...
		// 1. get input
		input = Game::get_input();

		// 2. move player
		Game::move(input);

		// 3. may or may not encounter events - moved before getting input in order to
		//	  display the percepts and player status on the same line closer to the player's eyesight 
		Game::check_event();

		// cout << "Checked for events on player position..." << endl; // Internal debugging use

		//Broken code; can't figure out how to restart the game
		// if (game_won || game_over) {
		// 	start_over();
		// }

	}
}