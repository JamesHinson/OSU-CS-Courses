#ifndef GOLD_H
#define GOLD_H 

#include <iostream>
#include "event.h"

//Gold Interface

class Gold : public Event {
	protected:
		string percept_message;
		
	public:	
		Gold();
		string get_percept();
};

#endif