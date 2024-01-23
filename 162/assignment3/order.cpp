#include "order.h"

using namespace std;

//function definitions from order.h goes here

Order::Order() {
	this->id = 0;
	this->coffee_name = "";
	this->coffee_size = 'E'; // E for empty size
	this->quantity = 0;
}

// id is the order number for order, so it should start at 1 and increase accordingly
void Order::set_id(const int id) {
	this->id = id + 1; 
	return;
}


void Order::set_coffee_name(const string coffee_name) {
	this->coffee_name = coffee_name;
	return;
}


void Order::set_coffee_size(const char coffee_size) {
	this->coffee_size = coffee_size;
	return;
}


void Order::set_quantity(const int quantity) {
	this->quantity = quantity;
	return;
}


int Order::get_id() const {
	return this->id;
}

string Order::get_coffee_name () const {
	return this->coffee_name;
}

float Order::get_coffee_size () const {
	return this->coffee_size;
}

float Order::get_quantity () const {
	return this->quantity;
}

// print the order object
void Order::print_order() const {
	return;
}