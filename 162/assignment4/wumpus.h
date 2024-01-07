#ifndef WUMPUS_H
#define WUMPUS_H 

#include <iostream>
#include "event.h"

// Wumpus Interface


class Wumpus : public Event {
	protected:
		string percept_message;
		bool alive;

	public:	
		Wumpus();
		
		string get_percept();
		bool get_alive();
};

#endif