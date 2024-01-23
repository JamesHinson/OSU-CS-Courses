#include "stalactites.h"

#include <iostream>

using namespace std;

// Stalactites Implementation
Stalactite::Stalactite() {
	percept_message = "You hear water dripping.\n";
	event_icon = 'V';
}

string Stalactite::get_percept() {
	return percept_message;
}