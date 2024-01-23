#ifndef STALACTITES_H
#define STALACTITES_H 

// Stalactites Interface

#include <iostream>
#include "event.h"

class Stalactite : public Event {
	protected:
		string percept_message;

	public:	
		Stalactite();

		string get_percept();
};

#endif