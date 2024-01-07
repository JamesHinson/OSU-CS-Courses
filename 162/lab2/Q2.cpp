/* CS 162- Lab 1 - Q.2
 * Solution description: call the function foo using "reference" to see the values before and after the function
 */
 
#include <iostream>

using namespace std;

int foo(int* a, int& b, int c){
    /*Set a to double its original value*/
    *a = *a * 2;

    /*Set b to half its original value*/
    b = b / 2;

    /*Assign a+b to c*/
    c = *a + b;

    /*Return c*/

    return c;
}

int main(){
    /*Declare three integers x,y and z and initialize them to 7, 8, 9 respectively*/
    int x = 7;
    int y = 8;
    int z = 9;
    int foo_results;

    /*Print the values of x, y and z*/
    cout << "x: " << x << endl;
    cout << "y: " << y << endl;
    cout << "z: " << z << endl;

    /*Call foo() appropriately, passing x,y,z as parameters*/
    foo_results = foo(&x, y, z);

    /*Print the value returned by foo*/
    cout << "foo results: " << foo_results << endl;

    /*Print the values of x, y and z again*/
    cout << "x: " << x << endl;
    cout << "y: " << y << endl;
    cout << "z: " << z << endl;

    /*Is the return value different than the value of z?  Why? */

    // The return value of z is the same as the initial value of z because no 
    return 0;
}
    
    
