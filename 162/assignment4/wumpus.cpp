#include "wumpus.h"

#include <iostream>

using namespace std;

// Wumpus Implementation
Wumpus::Wumpus() {
	percept_message = "You smell a terrible stench.\n";
	alive = true;
	event_icon = 'W';
}

string Wumpus::get_percept() {
	return percept_message;
}

bool Wumpus::get_alive() {
	return alive;
}