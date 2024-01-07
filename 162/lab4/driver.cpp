#include <iostream>
#include <fstream>

#include "student_db.h"


using namespace std;


int main()
{
	ifstream input;

	input.open("input.txt");

	int size;

	input >> size;

	student students = create_student_db(size);

	populate_student_db(students, 1, input);

	delete_student_db(students);

	return 0;
}