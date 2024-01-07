#include <iostream>
#include "coffee.h"

using namespace std;

// function definitions from coffee.h goes here

Coffee::Coffee() { // This might cause an error in the future if it takes up a space in the coffee array
	this->small_cost = 0;
	this->medium_cost = 0;
	this->large_cost = 0;
}

void Coffee::set_name (const string new_name) {
	this->name = new_name;
}


void Coffee::set_small_cost(const float new_small_cost) {
	this->small_cost = new_small_cost;
}


void Coffee::set_medium_cost(const float new_medium_cost) {
	this->medium_cost = new_medium_cost;
}


void Coffee::set_large_cost(const float new_large_cost) {
	this->large_cost = new_large_cost;
}


string Coffee::get_name() const {
	return this->name;
}


float Coffee::get_small_cost () const {
	return this->small_cost;
}


float Coffee::get_medium_cost () const {
	return this->medium_cost;
}


float Coffee::get_large_cost () const {
	return this->large_cost;
}


//print the coffee object
void Coffee::print_coffee() const {
	cout << this->name << endl;
	cout << this->small_cost << endl;
	cout << this->medium_cost << endl;
	cout << this->large_cost << endl;
}
