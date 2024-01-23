#include <iostream>

using namespace std;

int* create_array1(int size) {
	int *nums = new int [size];
	return nums;
}

void create_array2(int *& array, int size) {
	array = new int [size];
}

void create_array3 (int ** array, int size) {
	*array = new int [size];
}


int main()
{

	int size;
	int* array_1 = NULL;
	int* array_2 = NULL;
	int* array_3 = NULL;

	cout << "Input the size of your array: ";
	cin >> size;

// (1 pt) Next, in your main(), write three function calls to use the functions that you created above. 

	array_1 = create_array1(size);

	create_array2(array_2, size);

	create_array3(&array_3, size);

// (1 pt) Lastly, we need to manually free/delete the heap memory allocated to avoid memory leaks. Use delete operator to delete the memory off the heap. Make sure you set your pointer(s) back to NULL, since it is not supposed to be pointing anywhere anymore. 

	delete [] array_1;
	delete [] array_2;
	delete [] array_3;

	return 0;
}