#include <iostream>

#include "display.h"
#include "shop.h"

using namespace std;

void display_menu() {
	cout << "Choose an option:" << endl;
	cout << "1. Buy a lemonade" << endl;
	cout << "2. Buy a cookie" << endl;
	cout << "3. Quit" << endl;
}

void menu_loop() {
	shop s;
	int option;
	// This loop should keep running until either
	// A. The user types "3",
	// OR
	// B. The shop runs out of lemonade and cookies
	do {
		s.display_info();
		display_menu();
		cin >> option;

		if (option == 1) {
			if (s.out_of_lemonades()) {
				cout << "Sorry! We're out of stock" << endl;
			} else {
				s.buy_lemonade();
			}
		} else if (option == 2) {
			if (s.out_of_cookies()) {
				cout << "Sorry! We're out of stock" << endl;
			} else {
				s.buy_cookie();
			}
		}
		cout << endl << endl;
	} while (option == 3 || s.out_of_stock());
}
