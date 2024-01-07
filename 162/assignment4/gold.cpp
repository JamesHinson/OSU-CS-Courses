#include "gold.h"

#include <iostream>

using namespace std;

// Gold Implementation
Gold::Gold() {
	percept_message = "You see a glimmer nearby.\n";
	event_icon = '$';
}

string Gold::get_percept() {
	return percept_message;
}