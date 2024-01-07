#include <iostream>
#include <string>

using namespace std;

void get_sentence(string *s){
	cout << "Enter a sentence: ";
	getline(cin, *s);
}

int main()
{
	string sentence;

	get_sentence(sentence);
	cout << sentence << endl;

	return 0;
}