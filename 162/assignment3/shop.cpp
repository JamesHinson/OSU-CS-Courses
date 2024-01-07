#include "shop.h"

using namespace std;


// Default shop constructor - sets the variables to a default value of
// 0 or NULL depending on if they are an integer or an array
Shop::Shop() {
	this->revenue = 0;
	this->order_arr = NULL;
	this->num_orders = 0;
}

// Copy constructor - allows a user to copy all data from an existing shop
// to another existing shop
Shop::Shop(const Shop& new_shop) {

	this->num_orders = new_shop.num_orders;
	this->order_arr = new Order;

	for (int i = 0; i < this->num_orders; i++)
	{
		this->order_arr[i] = new_shop.order_arr[i];
	}
}

// Destructor - frees all dynamic memory present in the current shop if
// the memory was properly allocated and is still in use
Shop::~Shop() { // destructor
	if (this->order_arr != NULL) {

		delete [] this->order_arr;

		this->order_arr = NULL;
	}
}

// Assignment operator overload - allows a user to copy all data from an existing shop
// to a new shop
Shop& Shop::operator=(const Shop& new_shop) {

	if (this == & new_shop) {
		return *this;
	}

	if (this->order_arr != NULL) {
		delete [] this->order_arr;
	}

	this->num_orders = new_shop.num_orders;
	this->order_arr = new Order; //[this->num_orders];

	for (int i = 0; i < this->num_orders; i++)
	{
		this->order_arr[i] = new_shop.order_arr[i];
	}

	return *this;
}



// This function sets the revenue of the current Shop to a different integer
void Shop::set_revenue(const float revenue) {
	this->revenue = revenue;
	return;
}


// This function sets the order array of the current Shop to a different order array
void Shop::set_order_arr(Order* new_order_arr) {
	this->order_arr = new_order_arr;
	// array_length = this->order_arr.size(); // A new order is created, so you need to add to the array,
	// this->order_arr[array_length - 1] = new_order; // not overwrite it. Planning for this to work soon.
	return;
}


// This function sets the number of orders from the current Shop to a different integer
void Shop::set_num_orders(const int num_orders) {
	this->num_orders = num_orders;
	return;
}


// This function gets the revenue from the current Shop and returns it
float Shop::get_revenue() const { 
	return this->revenue;
}


// This function gets the order array from the current Shop and returns it
Order* Shop::get_order_arr() {
	return this->order_arr;
}

// This function gets the number of orders from the current Shop and returns it
int Shop::get_num_orders() const {
	return this->num_orders;
}


// This function loads the menu & shop info by reading the shop_info.txt file, and
// saves it to the current shop
void Shop::load_data() {
	// reads from files to correctly populate coffee, menu, etc.
	// Your code goes here:

	ifstream shop_info;
	shop_info.open("shop_info.txt");

	ifstream menu;
	menu.open("menu.txt");

	int num_coffee;

	menu >> num_coffee;

	Coffee temp_coffee;
	string temp_name;
	float temp_price = 0;

	Coffee* temp_coffee_array[num_coffee];

	// Uses the number of drinks multiplied by the number of items in a line of text
	// to add the name & price of each type of coffee to a temp coffee array.
	// This temp array is used below to load the current menu/coffee array.
	// Possibly turn this into its own member function of shop or menu?
	for (int i = 0; i < num_coffee * 4; i++) 
	{
		*temp_coffee_array[i] = temp_coffee;
		menu >> temp_name;
		temp_coffee.set_name(temp_name);
		menu >> temp_price;
		temp_coffee.set_small_cost(temp_price);
		menu >> temp_price;
		temp_coffee.set_medium_cost(temp_price);
		menu >> temp_price;
		temp_coffee.set_large_cost(temp_price);
	}

	// Sets up the current coffee array using the information found in the menu.txt file
	this->m.set_coffee_arr(*temp_coffee_array);

	string temp_phone;
	string temp_addr;

	shop_info >> temp_phone;

	this->phone = temp_phone;

	getline(shop_info, temp_addr);
	getline(shop_info, temp_addr);

	this->address = temp_addr;

	cout << "Shop::load_data() completed successfully..!" << endl;

	shop_info.close(); // In case of any memory leaks based on not closing the files,
	menu.close();	   // which was seen in Assignment 2 and pointed out by a TA as the likely cause.
	return;
}

// This function gets the shop info and menu from the current Shop and displays it
void Shop::view_shop_detail() {
	//handle "View shop detail" option
	//print shop address, phone number, revenue, menu, and order
	//Your code goes here: 

	cout << "Address: " << this->address << endl;
	cout << "Phone: " << this->phone << endl;
	cout << "The total shop revenue is: $" << this->revenue << endl;
	cout << "\nHere is our menu:" << endl;

	// Assigns local variables to member information for easier use with functions
	int num_coffee = this->m.get_num_coffee();
	Coffee* coffee_array = this->m.get_coffee_arr();
	Order* order_array = get_order_arr();

	// Prints the current menu information to the screen
	for (int i = 0; i < num_coffee; i++)
	{
		cout << (i + 1) << "." << coffee_array[i].get_name() << endl;
		cout << "   " << "Small - " << coffee_array[i].get_small_cost() << endl;
		cout << "   " << "Medium - " << coffee_array[i].get_medium_cost() << endl;
		cout << "   " << "Large - " << coffee_array[i].get_large_cost() << endl;
		cout << endl;
	}

	cout << "Order info:" << endl;

	if (this->num_orders != 0)
	{
		for (int i = 0; i < this->num_orders; i++)
		{
			cout << order_arr[i].get_id();
			cout << " " << order_arr[i].get_coffee_name();
			cout << " " << order_arr[i].get_coffee_size();
			cout << " " << order_arr[i].get_quantity();
			cout << endl;
		}
	} else {
		cout << "(No orders to display)" << endl;
	}

	cout << "\nShop::view_shop_detail() completed successfully..!" << endl;
	// cout << "Shop::view_shop_detail() not implemented..." << endl;

	return;
}

// This function adds a new product to the current Shop
void Shop::add_to_menu() {
	//handle "Add coffee to menu" option
	//Hint: call Menu::add_to_menu(Coffee& coffee_to_add);
	//Your code goes here: 
	cout << "Shop::add_to_menu() not implemented..." << endl;

	return;
}

// This function removes a product from the current Shop
void Shop::remove_from_menu() {
	//handle "Remove coffee from menu" option
	//Hint: call Menu::remove_from_menu(int index_of_coffee_on_menu);
	//Your code goes here: 
	cout << "Shop::remove_from_menu() not implemented..." << endl;

	return;
}

// This function allows a user to search for a product by name in the current shop menu
void Shop::search_by_name(){
	//handle "Search by coffee name" option
	//Hint: call Menu::search_coffee_by_name(string name);
	//Your code goes here: 
	cout << "Shop::search_by_name() not implemented..." << endl;

	return;
}

// This function allows a user to search for a product by price in the current shop menu
void Shop::search_by_price() {
	//handle "Search by coffee price" option
	//Hint: call Menu::search_coffee_by_price(float budget);
	//Your code goes here: 
	cout << "Shop::search_by_price() not implemented..." << endl;

	return;
}

// This function allows a user to place a new order for the current shop
void Shop::place_order() {
	//handle "Place order" option
	//Your code goes here: 
	cout << "Shop::place_order() not implemented..." << endl;

	return;
}

// This function allows the user to clone all of the contents of a current shop,
// performing a deep copy of dynamic memory
Shop Shop::clone_shop() {
	//handle "Clone a shop" option
	//note: the purpose of this option is to test
	//your big three implementation
	Shop cloned_shop;

	cloned_shop = *this; // test AOO        

    Shop cloned_shop2 = *this; // test CC 

    cout << "Shop cloned successfully!" << endl; 

    return cloned_shop;
}