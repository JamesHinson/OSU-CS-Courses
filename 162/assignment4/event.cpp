#include "event.h"

#include <iostream>

using namespace std;

// Event Implementation

Event::Event() {
	percept_message = " ";
	event_icon = ' ';
}

string Event::get_percept() {
	return percept_message;
}

void Event::display_percept() {
	cout << percept_message << endl;
}