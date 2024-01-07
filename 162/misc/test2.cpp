#include <iostream>
#include <random>

using namespace std;


int random_number(int input) {
	int random_room = rand() % input;
	cout << "Randomly selected number: " << random_room << endl; // Debug purposes
	return random_room;
}

int main()
{
	srand(time(NULL));

	int input = 5;

	int x = random_number(input);

	cout << x << endl;

	x = random_number(input);

	cout << x << endl;
	
	return 0;
}