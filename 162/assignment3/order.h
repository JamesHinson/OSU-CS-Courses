#ifndef ORDER_H
#define ORDER_H 

#include <string>

using namespace std;

class Order
{
private:
	int id;
	string coffee_name;
	char coffee_size;
	int quantity;

public:
	// need to include accessor functions and mutator functions for private member when appropriate
    // need to include constructors and destructors where appropriate
    // need to use 'const' when appropriate
    Order();       // Order constructor
    void set_id (const int);
    void set_coffee_name(const string); 
    void set_coffee_size(const char);
    void set_quantity(const int);

    int get_id() const;
    string get_coffee_name() const;
    float get_coffee_size() const;
    float get_quantity() const;

    void print_order() const; // print the order object
};
#endif