/******************************************************
** Program: stairs.cpp
** Author: James Hinson
** Date: 12/7/2023
** Description: The secondary program file for the ways_to_top
**              recursion exercise - calculates the ways to
**              the top of a staircase of 'n' stairs.
**
** Input: User input for the total number of steps.
**
** Output: Returns the number of unique ways to the
**         top of a staircase of 'n' stairs.
******************************************************/



/*********************************************************************
** Function: ways_to_top
** Description: Calculates the number of unique ways to reach the top
**              of a staircase of 'n' stairs using a recursive approach.
**              The function counts the distinct ways to climb the
**              staircase by taking steps of sizes 1, 2, or 3.
**
** Parameters: n, ways
** Pre-Conditions: The function must be called with a non-negative integer.
** Post-Conditions: The number of unique ways to get to the
**                  top of a staircase of 'n' stairs is returned.
*********************************************************************/
int ways_to_top(int n) {

    // Base cases:
    if (n == 0) {

        // If there are 0 steps, there is only one way to reach the top (no steps taken).
        // Could also be perceived as zero ways to reach the top, since there is no "top".
        return 1;

    } else if (n < 0) {

        // If the number of steps is negative, there is no way to reach the top.
        return 0;
    }

    // Recursive calls considering taking 1, 2, or 3 steps at a time.
    int ways = 0;
    ways += ways_to_top(n - 1); // Take a small step (size 1)

    if (n >= 2) {
        ways += ways_to_top(n - 2); // Take a medium step (size 2)
    }
    if (n >= 3) {
        ways += ways_to_top(n - 3); // Take a large step (size 3)
    }

    return ways;
}
