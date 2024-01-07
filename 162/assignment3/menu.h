#ifndef MENU_H
#define MENU_H 

#include <string>
#include <fstream>
#include "coffee.h"

using namespace std;

class Menu {
  private:
    int num_coffee;
    Coffee* coffee_arr;
  public:
    //need to include accessor functions and mutator functions for private member when appropriate
    //need to include constructors, copy constructors, assignment operator overload,
    //and destructors where appropriate
    //need to use 'const' when appropriate

    // Note: These 4 are needed any time you have dynamic memory in classes
    Menu();
    Menu(const Menu&); // copy constructor
    Menu& operator=(const Menu&); // assignment operator overload
    
    Menu(int size) { // Non-standard constructor
      this->num_coffee = size;
      this->coffee_arr = new Coffee [size];
    }

    ~Menu(); // destructor

    int get_num_coffee() const;
    Coffee* get_coffee_arr() ;

    void set_num_coffee(const int);
    void set_coffee_arr(Coffee*);



    // Suggested functions:
    Coffee search_coffee_by_name(string name); 
    Menu search_coffee_by_price(float budget); 
    void add_to_menu(Coffee& coffee_to_add); // add a coffee object into the Menu
    void remove_from_menu(int index_of_coffee_on_menu); // remove a coffee object from the Menu

    // feel free to add more member functions
};


#endif