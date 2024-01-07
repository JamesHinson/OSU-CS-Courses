#include <iostream>
#include <fstream>

using namespace std;


student * create_student_db(int size) {
	students = new student[size];
	return students;
}


void populate_student_db_info(student *students, int line, ifstream &input) {
	
}


void delete_student_db_info(student *&) {
	delete [] students;
	students = nullptr;
}
