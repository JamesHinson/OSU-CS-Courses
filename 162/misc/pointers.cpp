#include <iostream>

using namepsace std; 

void change_me(int* x) {
	*x = 0;
}

void change_me_ref(int& x) {
	x = 0;
}


int main()
{
	int y = 10;
	int* p = &y;
	cout << p << endl; // Prints: the memory address for y

	*p = 100; // Equivalent to: y = 100
	cout << y << endl; // Prints: 100
	cout << *p << endl; // Prints: 100


	change_me(&y); // OR change_me(p) - these are equivalent
	cout << y << endl; // Print: 100


	int& ref = y;
	ref = 3;

	cout << y << endl; // Prints: 3

	change_me_ref(y);

	ref = x; // What does this do? y = x

	const int* const_p = &y; // A pointer to a constant int

	cout << const_p << endl;


	/*

	Pointers:
		Context 1: In the declaration of a variable (int* p)
		Meaning: We are declaring a pointer to an int

		Context 2: Prefix to existing pointer (*p)
		Meaning: Dereference operator: go to that memory address,
		and access the vlaue in that box

	References:
		Context 1: Prefix to existing variable (&y)
		Meaning: Get the address of y
		
		Context 2: In the declaration of a variable, (int& ref = y;)
		Meaning: ref is a reference to an integer (y)
	*/


	/*
		
	string* my_string_pointer; 
	*my_string_pointer = "Hello";

	^^^ This is garbage! - this is a memory address with an arbitrary value.
	Nothing has been allocated and no variable initialized, so it will
	overwrite any data present at this address.

	*/

	return 0;
}