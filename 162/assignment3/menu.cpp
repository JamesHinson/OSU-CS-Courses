#include "menu.h"

using namespace std;


// Default menu constructor - sets the variables to a default value of
// 0 or NULL depending on if they are an integer or an array
Menu::Menu() {
	this->num_coffee = 0;
	this->coffee_arr = NULL;
}

// Copy constructor - allows a user to copy all data from an existing menu
// to another existing menu
Menu::Menu(const Menu& new_menu) { // copy constructor

	this->num_coffee = new_menu.num_coffee;
	this->coffee_arr = new Coffee [this->num_coffee];

	for (int i = 0; i < this->num_coffee; i++)
	{
		this->coffee_arr[i] = new_menu.coffee_arr[i];
	}
}

// Assignment operator overload - allows a user to copy all data from an existing shop
// to a new shop
Menu& Menu::operator=(const Menu& new_menu) { // assignment operator overload

	if (this == & new_menu) {
		return *this;
	}

	if (this->coffee_arr != NULL) {
		delete [] this->coffee_arr;
	}

	this->num_coffee = new_menu.num_coffee;
	this->coffee_arr = new Coffee [this->num_coffee];
	for (int i = 0; i < this->num_coffee; i++)
	{
		this->coffee_arr[i] = new_menu.coffee_arr[i];
	}

	return *this;
}

// Destructor - frees all dynamic memory present in the current shop if
// the memory was properly allocated and is still in use
Menu::~Menu() {
	if (this->coffee_arr != NULL) {

		delete [] this->coffee_arr;

		this->coffee_arr = NULL;
	}
}

// This function sets the number of coffee types from the current Menu to a different integer
void Menu::set_num_coffee (const int num_coffee) {
	this->num_coffee = num_coffee;
	return;
}

// This function sets the coffee array of the current Shop to a different coffee array
void Menu::set_coffee_arr (Coffee* new_coffee_arr) {
	this->coffee_arr = new_coffee_arr;
	return;
}

// This function gets the number of coffee types from the current Menu and returns it
int Menu::get_num_coffee() const {
	return this->num_coffee;
}

// This function gets the coffee array from the current Menu and returns it
Coffee* Menu::get_coffee_arr() {
	return this->coffee_arr;
}

// This function allows a user to search for a product by name in the current menu and returns it
Coffee Menu::search_coffee_by_name(string name) {
	Coffee found; 
	//search coffee with a specific name 
	//return the coffee if found 
	//Your code goes here: 

	return found;
}

// This function allows a user to search for a product by price in the current menu and returns it
Menu Menu::search_coffee_by_price(float budget){
	Menu temp;
	//search coffee with a specific budget 
	//return all coffee that is under the budget
	//Hint: Since a Menu object contains an array of coffee
	//      You may return a Menu object that contains all valid coffees
	//Your code goes here: 

	return temp;

}

// This function adds a new product to the current Menu
void Menu::add_to_menu(Coffee& coffee_to_add){
	//add a coffee object into the Menu
	//Your code goes here: 

	return;
} 

// This function removes a product from the current Menu
void Menu::remove_from_menu(int index_of_coffee_on_menu){
	//remove a coffee object from the Menu
	//Your code goes here: 

	return;
} 
