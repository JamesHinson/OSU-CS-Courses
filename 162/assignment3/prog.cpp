#include <iostream>
#include "display.h"

using namespace std;

int main()
{
	//your main function lives here
	cout << "Welcome to Coffee++" << endl;
	int choice = -1;
	Shop s;
	//populate your Shop:
	//your code here:

	while (choice != QUIT){
		choice = get_choice();
		perform_action(s, choice);
	}

	cout << "Bye!" << endl;

	return 0;
}
