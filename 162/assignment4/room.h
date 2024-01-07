#ifndef ROOM_H
#define ROOM_H 

#include "event.h"
#include "bats.h"
#include "gold.h"
#include "stalactites.h"
#include "wumpus.h"

using namespace std;

// Room Interface
// Note: Each room may be empty or have an event (gold, Wumpus, stalacatites, or bats);
//		Use event polymorphically

class Room {
	protected:
		Event *inRoom; // Each room only has one event
		char event;
		char player; 

	public:	
		// Default Constructor
		Room();
		
		// Accessors
		char get_event() const;
		char get_player() const;
		string get_percepts() const;
		
		// Mutators
		void set_player(char);
		void set_event(char);
		void set_wumpus();
		
		// Deconstructor
		~Room();
};

#endif