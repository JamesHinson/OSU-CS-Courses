#include <iostream>
#include "linked_list.h"

using namespace std;

void pause() {
        cout << "\n\nPress <enter> to continue...";
        cin.clear();
        cin.ignore(256, '\n');
}


int main(int argc, char const *argv[]) {
	Linked_List l;

	//if doing EC (template), use the following line instead:
	//Linked_List <int> l;

	cout << "##################################" << endl;
	cout << "###	     Test Cases        ###" << endl;
	cout << "##################################" << endl;
	
	cout << "\n\nList successfully created!!\n\n";;

	cout << "**********Test 1***********\n";
	cout << "Before adding nodes...\n";
	cout << "Testing get_length()\n";
	cout << "Expected: 0\n";
	cout << "Actual  : " << l.get_length() << "\n";
	if (l.get_length() == 0)
		cout << "Test 1 PASSED\n\n";
	else
		cout << "Test 1 FAILED\n\n";
	pause();

	cout << "**********Test 2***********\n";
	cout << "Adding nodes...\n";
	cout << "Test 2.1: Testing push_front()\n";
	l.push_front(5);
	l.push_front(100);
	l.push_front(0);
	l.push_front(-8);
	l.push_front(16);
	cout << "Expected: 16 -8 0 100 5\n";
	cout << "Actual  : "; 
	l.print();
	cout << "Expected length: 5\n";
	cout << "Actual length  : " << l.get_length() << "\n";
	cout << "Test 2.1 completed.\n";
	pause();

	cout << "Removing nodes...\n";
	cout << "Test 2.2: Testing pop_front()\n";
	l.pop_front();
	l.pop_front();
	l.pop_front();
	cout << "Print list...\n";
	cout << "Expected: 100 5\n";
	cout << "Actual  : "; 
	l.print();
	cout << "Expected length: 2\n";
	cout << "Actual length  : " << l.get_length() << "\n";
	pause();

	cout << "Continue removing...\n";
	l.pop_front();
	l.pop_front();
	l.pop_front(); // no more nodes, shouldn't remove anything 
	cout << "Print list...\n";
	cout << "Expected: \n";
	cout << "Actual  : "; 
	l.print();
	cout << "Expected length: 0\n";
	cout << "Actual length  : " << l.get_length() << "\n";
	cout << "Test 2.2 completed.\n";
	pause();

	cout << "Adding nodes...\n";
	cout << "Test 2.2: Testing push_back()\n";
	l.push_back(5);
	l.push_back(1);
	l.push_back(2);
	l.push_back(7);
	l.push_back(7919);
	cout << "Expected: 5 1 2 7 7919\n";
	cout << "Actual  : "; 
	l.print();
	cout << "Expected length: 5\n";
	cout << "Actual length  : " << l.get_length() << "\n";
	cout << "Test 2.3 completed.\n";
	pause();

	cout << "Removing nodes...\n";
	cout << "Test 2.4: Testing pop_back()\n";
	l.pop_back();
	l.pop_back();
	cout << "Print list...\n";
	cout << "Expected: 5 1 2\n";
	cout << "Actual  : "; 
	l.print();
	cout << "Expected length: 3\n";
	cout << "Actual length  : " << l.get_length() << "\n";
	pause();

	cout << "Continue removing...\n";
	l.pop_back();
	l.pop_back();
	l.pop_back();
	l.pop_back(); // no more nodes, shouldn't remove anything 
	cout << "Print list...\n";
	cout << "Expected: \n";
	cout << "Actual  : "; 
	l.print();
	cout << "Expected length: 0\n";
	cout << "Actual length  : " << l.get_length() << "\n";
	cout << "Test 2.4 completed.\n";
	pause();

	cout << "Adding nodes...\n";
	l.push_front(5);
	l.push_front(100);
	l.push_front(0);
	l.push_front(-8);
	l.push_front(16);
	l.push_back(5);
	l.push_back(1);
	l.push_back(2);
	l.push_back(7);
	l.push_back(7919);
	cout << "Test 2.5: Testing insert()\n";
	l.insert(11, 0);   // insert 11 at the front of the list
	l.insert(20, 100); // 100 is not a valid index, therefore 20 is not inserted
	l.insert(50, l.get_length()); // insert 50 at the end of the list
	l.insert(9, 5); // insert 9 at index 5 
	cout << "Expected: 11 16 -8 0 100 9 5 5 1 2 7 7919 50\n";
	cout << "Actual  : "; 
	l.print();
	cout << "Expected length: 13\n";
	cout << "Actual length  : " << l.get_length() << "\n";
	cout << "Test 2.5 completed.\n";
	pause();

	cout << "Removing nodes...\n";
	cout << "Test 2.6: Testing remove()\n";
	l.remove(9);   // remove the node with index 9 (value 2) of the list
	l.remove(100); // 100 is not a valid index, therefore no node is removed
	l.remove(l.get_length() - 1); // remove the last node (value 50) in the list
	l.remove(0); // remove the first node (11) in the list 
	cout << "Expected: 16 -8 0 100 9 5 5 1 7 7919\n";
	cout << "Actual  : "; 
	l.print();
	cout << "Expected length: 10\n";
	cout << "Actual length  : " << l.get_length() << "\n";
	cout << "Test 2.6 completed.\n";
	pause();


	cout << "**********Test 3***********\n";
	cout << "Sorting...\n";
	cout << "Test 3.1: Testing sort_ascending()\n";
	l.sort_ascending();
	cout << "Expected: -8 0 1 5 5 7 9 16 100 7919\n";
	cout << "Actual  : "; 
	l.print();
	cout << "Test 3.1 completed.\n";
	pause();

	cout << "Test 3.2: Testing sort_descending()\n";
	l.sort_descending();
	cout << "Expected: 7919 100 16 9 7 5 5 1 0 -8\n";
	cout << "Actual  : "; 
	l.print();
	cout << "Test 3.2 completed.\n";
	pause();

	cout << "**********Test 4***********\n";
	cout << "Tesing clear()\n";
	l.clear();
	cout << "Expected length: 0\n";
	cout << "Actual length  : " << l.get_length() << "\n";
	if (l.get_length() == 0) {
		cout << "Test 4 PASSED\n";
	} else {
		cout << "Test 4 FAILED\n";
	}

	cout << "Run valgrind to check memory leaks/errors\n" << endl; 

	cout << "##################################" << endl;
	cout << "###	   End Test Cases      ###" << endl;
	cout << "##################################" << endl;

	return 0;
}
