#include <iostream>

using namespace std;

//Define a struct of Person type
struct Person
{
	string name; 
	int age;
};

/***********************************************
 * Function name: create_person_array
 * Description: allocate memory for an array of Person, with size provided
 * Parameters: size  - size of the array
 * Pre-conditions: None
 * Post-conditoins: an array of Person is created, and return the address
 ***********************************************/
Person* create_person_array (int size){
	Person *array = new Person [size];
	return array;
}

/***********************************************
 * Function name: init_person_array
 * Description: initialize the array of Person with user inputs,
 		        with the array and size provided
 * Parameters: array - pointer to the Person array
               size  - size of the array
 * Pre-conditions: the Person array has been created/allocated
 * Post-conditoins: an array of Person is populated with user inputs
 ***********************************************/
void init_person_array (Person* array, int size){
	for (int i = 0; i < size; ++i)
	{
		cout << "Enter name for Person " << i+1 << ": ";
		cin >> array[i].name;
		cout << "Enter age for Person " << i+1 << ": ";
		cin >> array[i].age; 
		cout << endl;
	}
	return;
}

/***********************************************
 * Function name: print_person_array
 * Description: print the array of Person,
 		        with the array and size provided
 * Parameters: array - pointer to the Person array
               size  - size of the array
 * Pre-conditions: the Person array has been created/allocated
 * Post-conditoins: an array of Person is printed to the screen
 ***********************************************/
void print_person_array (Person* array, int size){
	for (int i = 0; i < size; ++i)
	{
		cout << "Person " << i+1 << ": " << endl;
		cout << "Name: " << array[i].name << endl;
		cout << "Age: " << array[i].age << endl;
		cout << endl;
	}
	return;
}

/***********************************************
 * Function name: delete_person_array
 * Description: free the memory allocated by the array of Person 
 * Parameters: array - pointer to the Person array
 * Pre-conditions: None
 * Post-conditoins: the memory allocated by the array of Person is freed
 ***********************************************/
void delete_person_array (Person* array){
	delete [] array;

	return;
}

int main()
{
	//prompt the user for the size of the array
	int size = -1;
	cout << "Enter number of people: ";
	cin >> size;

	//allocate memory
	Person *ppl = create_person_array(size);

	//initialize/populate the array
	init_person_array(ppl, size);

	//print the array
	print_person_array(ppl, size);

	//delete the array
	delete_person_array(ppl);
	ppl = nullptr;


	return 0;
}