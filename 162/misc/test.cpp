#include <iostream>
#include <string>

using namespace std;

void init_times_table (int** table, int rows, int cols) {
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			table[i][j] = (i + 1) * (j + 1);
			cout << table[i][j] << " " << endl;
		}
	}
}


int main() {

	string my_str[10];
	int my_str_len = (sizeof(my_str)/sizeof(*my_str));

	cout << my_str_len << endl;

	int rows;
	cout << "How many rows? ";
	cin >> rows;

	int cols;
	cout << "How many columns? ";
	cin >> cols;

	int** times_table = new int*[rows];
	for (int i = 0; i < rows; i++) {
		times_table[i] = new int[cols];
	}

	init_times_table(times_table, rows, cols);
	return 0;
}