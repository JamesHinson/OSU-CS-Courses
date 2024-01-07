#ifndef BATS_H
#define BATS_H 

#include <iostream>
#include "event.h"

// Bats Interface

class Bats : public Event{
	protected:
		string percept_message;

	public:	
		Bats();
		string get_percept();
		void display_percept();
};

#endif