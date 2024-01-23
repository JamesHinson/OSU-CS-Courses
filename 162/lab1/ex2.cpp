#include <iostream>

using namespace std;


// function() determines whether or not an integer is odd or even

void function(int num, int ctr, int &r) { // reference r
    int i;
    for (i = 2; i <= num / 2; i++) { // 2 <= num / 2
        if (num % i == 0) { // if num divides by i evenly, add 1 to the counter and break
            ctr++;
            break;
        }
    }
    if (ctr == 0 && num != 1) { // if counter is 0 and num != 1 (an odd number)
        r = 1; // set r to 1
    } else {                    // else, number is even
        r = 0; // set r to 0
    }
}

int main()
{
    int num, ctr = 0, r = -1;
    cout << "Input a number: ";
    cin >> num;

    function(num, ctr, r);
    cout << r << endl; // print r - 0 for even and 1 for odd

    return 0;
}


/*
Outputs:

num = 7 | r = 1

num = 5 | r = 1

num = 4 | r = 0

num = 2 | r = 0

num = 1 | r = 0

*/