#include "room.h"

using namespace std;

// Room Implementation
Room::Room() {
	event = ' ';
	inRoom = nullptr;
	player = ' ';
}

// Only frees memory if inRoom is a valid address (already pointing to something)
Room::~Room() {
	if (inRoom != nullptr) {
		delete inRoom;
	}
}

char Room::get_event() const {
	return event;
}

char Room::get_player() const {
	return player;
}

// Avoids dealing with the comparing null to a string error by only calling the function
// on known-valid cases (no null)
string Room::get_percepts() const {
	switch (event) {
		case 'W':
			return "You smell a terrible stench.\n";
		    // return inRoom->get_percept();
		case 'B':
			return "You hear wings flapping.\n";
		    // return inRoom->get_percept();
		case 'V':
			return "You hear water dripping.\n";
		    // return inRoom->get_percept();
		case '$':
			return "You see a glimmer nearby.\n";
		    // return inRoom->get_percept();
    	default:
    		return "";
    }
}

void Room::set_player(char input) {
	player = input;
}

void Room::set_event(char event) {

	this->event = event;

	switch (event) {
		case 'W':
		    inRoom = new Wumpus;
		    break;
		case 'B':
		    inRoom = new Bats;
		    break;
		case 'V':
		    inRoom = new Stalactite;
		    break;
		case '$':
		    inRoom = new Gold;
		    break;
    	default:
    		inRoom = nullptr;
	        break;
    }
}