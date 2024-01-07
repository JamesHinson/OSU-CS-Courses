#include "bats.h"

#include <iostream>

using namespace std;

// Bats Implementation
Bats::Bats() {
	percept_message = "You hear wings flapping.\n";
	event_icon = 'B';
}

string Bats::get_percept() {
	return percept_message;
}

void Bats::display_percept(){
	cout << percept_message << endl;
}