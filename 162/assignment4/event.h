#ifndef EVENT_H
#define EVENT_H 

#include <iostream>
#include <string>

using namespace std;

// Event Interface
// Note: this must be an abstract class!

class Event {

protected:
	int event_row; // The location of the event in the rows of Room objects
	int event_col; // The location of the event in the columns of Room objects
	
	string percept_message; // Message to be displayed when the player is close to an event
	char event_icon; // The character to represent different events in Rooms

public:
	Event();
	virtual string get_percept();
	virtual void display_percept();
	
};

#endif