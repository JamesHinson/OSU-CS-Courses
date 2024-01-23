#include <iostream>

using namespace std;

struct multdiv_entry {
	int mult;
	float div;
};


//function prototypes
multdiv_entry** create_table(int row, int col);
void print_table(multdiv_entry** tables, int row, int col);
void delete_table(multdiv_entry** tables, int row);


int main()
{
	int row, col;

	multdiv_entry **temp_table;

	//Your code here:
	cout << "Enter an integer greater than zero for rows: ";
	cin >> row;

	cout << "\nEnter an integer greater than zero for columns: ";
	cin >> col;

	temp_table = create_table(row, col);
	cout << temp_table;

	return 0;
}

multdiv_entry** create_table(int row, int col){
	multdiv_entry** multdiv_entry[row][col];

	return **multdiv_entry;
}