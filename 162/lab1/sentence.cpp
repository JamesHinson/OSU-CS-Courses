#include <iostream>
#include <string>

using namespace std;

void get_sentence(string &sentence){ // changed "string s" to "string &s" in order to change the value 
        cout << "Enter a sentence: ";
        getline(cin, sentence);
}

int main()
{
        string sentence;

        get_sentence(sentence);
        cout << sentence << endl;

        return 0;
}

/*

1. What is indeed passed into the function if an ampersand (&) is added in front of the parameter?

        If an ampersand is added in front of the parameter, the value of 'sentence' from main()
        is passed to the get_sentence() function

2. Can we change the value of the string inside the function if we change the function prototype to:
        'void get_sentence(string &sentence);'
        
        No, not unless you also change the 's' in the getline() function within get_sentence().
        If you do change this, it will work.


3. What is the difference between pass by value vs. pass by reference?

        Pass by value only passes the value that a variable contains, whereas pass by reference effectively
        passes the variable itself, allowing it to be modified.

*/