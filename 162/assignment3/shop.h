#ifndef SHOP_H
#define SHOP_H

#include <string>
#include <fstream>
#include <iostream>
#include "menu.h"
#include "order.h"

using namespace std;

class Shop {
  private:
    Menu m;
    string phone;
    string address; 
    float revenue;      // shop revenue
    Order *order_arr;   // order array
    int num_orders;     // number of orders
  public:
    // need to include accessor functions and mutator functions for private member when appropriate
    // need to include constructors and destructors where appropriate
    // need to use 'const' when appropriate
    Shop();
    Shop(const Shop&); // copy constructor
    Shop& operator=(const Shop&); // assignment operator overload

    ~Shop(); // destructor

    void set_revenue(const float);    // revenue mutator (setter)
    void set_order_arr(Order*); // order_array mutator
    void set_num_orders(const int);   // num_orders mutator


    float get_revenue() const;        // revenue accessor (getter)
    Order* get_order_arr();      // order_array accessor
    int get_num_orders() const;       // num_orders accessor



    // Suggested functions
    void load_data(); // reads from files to correctly populate coffee, menu, etc.
    void view_shop_detail();
    void add_to_menu();
    void remove_from_menu();
    void search_by_name();
    void search_by_price();
    void place_order();
    Shop clone_shop();
    
};

#endif
