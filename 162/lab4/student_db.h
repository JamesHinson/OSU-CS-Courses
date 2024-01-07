#include <iostream>
#include <string>
#include <fstream>

using namespace std;


struct student {
	int id;
	string first_name;
	string last_name;
	string major;
	float gpa;
};

student * create_student_db(int);

void populate_student_db_info(student *, int, ifstream &);

void delete_student_db_info(student *&);