#ifndef GAME_H
#define GAME_H 

#include <vector>
#include <iostream> 
#include "room.h"

using namespace std;

// Game interface
class Game {
private:
	
	// declare a 2D vector of Room objects:
	vector<vector<Room>> map; // 2D vector of Room objects

	int length; 			// Length of the map
	int width;  			// Width of the map
	int num_arrows; 		// Keeps track of the number of arrows remaining

	bool debug_view;		// Whether or not debug view is active

	int map_size;
	int player_start_x;
	int player_start_y;
	int current_position_x;
	int current_position_y;

	char move_choice;

	bool carrying_gold;
	bool is_confused;
	int confused_timer;

	bool game_over;
	bool game_won;
	bool gold_at_start;
	bool wumpus_killed;


public:
	Game();
	~Game();
	
	void set_up(int, int);
	int get_dimension(string);

	void display_game() const;
	void display_percepts() const;

	bool check_win();
	void check_event();

	char get_dir();
	void wumpus_move();
	void fire_arrow();

	void move_up();
	void move_down();
	void move_left();
	void move_right();
	void move(char);

	char get_input();

	int set_random_room(int);

	void play_game(int, int, bool, bool);
	void start_over();

	bool in_bounds(int, int);
	bool is_debug(string);


};

#endif