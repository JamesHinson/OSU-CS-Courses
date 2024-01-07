#include <iostream>

using namespace std;

void function (int x[], int n) { // int array and int n
    int i, t, j = n, s = 1;
    while (s) { // while true
        s = 0; // while is now false
        for (i = 1; i < j; i++) { // j == n
            if (x[i] < x[i - 1]) { // checks the value of the array one index before the current index [i - 1]
                t = x[i];
                x[i] = x[i - 1];
                x[i - 1] = t;
                s = 1; // restart while loop
            }
        }
        j--; // subtracts after for loop, only when while loop restarts
    }
}

int main () {
    int x[] = {15, 56, 12, -21, 1, 659, 3, 83, 51, 3, 135, 0}; 
    int n = sizeof(x) / sizeof(x[0]); // gets the size of the array divided by x[0] in bytes
    int i;
    for (i = 0; i < n; i++) // i == j
        cout << x[i] << " ";
    cout << endl;

    function(x, n);

    for (i = 0; i < n; i++)
        cout << x[i] << " ";
    cout << endl;

    return 0;
}