/******************************************************************************
** Program Filename: money_ball.cpp
** Author: James Hinson
** Date: 10/17/2023
** Description: This is a short command-line basketball-inspired game 
** 				for two players, with the goal being to win the most 
**				points in one round, using 50/50 odds of successfully 
**				earning a point. It requires user input and the system clock.
**
** Input: User input to navigate menus and confirm placement of moneyball rack
** Output: Console output to display shots, points, winner, and menus
******************************************************************************/



// Header files for input/output and working with real-time data
#include <iostream>
#include <ctime>



/*********************************************************************
** Function: get_scores
** Description: Calculates the total scores for each player. Slightly
**				over 15 lines in order to accurately calculate scores.
**
** Parameters: reg_score, money_score, starry_score, money_rack, total_score
**
** Pre-Conditions: reg_score, money_score, starry_score, and money_rack 
** 				   must have integer values when the function is called.
**
** Post-Conditions: total_score must be returned as an integer
*********************************************************************/
int get_scores(int reg_score, int money_score, int starry_score, int money_rack) {

	reg_score = (reg_score - (money_score / 2));

	// if (money_rack == 1) {

	// 	money_score = money_score - 1;

	// } else if (money_rack == 2) {

	// 	reg_score = reg_score + 1;
	// 	money_score = money_score - 2;

	// } else if (money_rack == 3) {

	// 	reg_score = reg_score + 1;
	// 	money_score = money_score - 3;

	// } else if (money_rack == 4) {

	// 	reg_score = reg_score + 2;
	// 	money_score = money_score - 4;
	// }

	int total_score = reg_score + money_score + starry_score;

	std::cout << "\nYour Regular points are: " << reg_score << std::endl;
	std::cout << "Your Money Ball points are: " << money_score << std::endl;
	std::cout << "Your Starry Ball points are: " << starry_score << std::endl;

	std::cout << "Your total score is: " << total_score << std::endl;
	return total_score;
}



/*********************************************************************
** Function: money_ball_shots
** Description: Calculates and displays the shots made for each
**				moneyball in the round, then returns the score earned by
**				each money ball to be used later.
**
** Parameters: x, money_rack, player_shots, money_ball_score
**
** Pre-Conditions: money_rack must be determined by the user, and player_shots
**				   must be created before function call
**
** Post-Conditions: money_ball_score must be returned as an integer
*********************************************************************/
int money_ball_shots(int money_rack, char player_shots[][5]) {
	int x;
	int money_ball_score = 0;

	for (int i = 0; i < 5; i++) {
		std::cout << "Rack " << i + 1 << ": ";
		for (int j = 0; j < 5; j++) {
			if ((j == 4 && player_shots[i][j] == 'O') || (i == money_rack && player_shots[i][j] == 'O')) {
				money_ball_score += 2;
				player_shots[i][j] = 'M';
			}
			std::cout << player_shots[i][j] << " ";
		}
		std::cout << std::endl;
	}
	return money_ball_score;
}



/*********************************************************************
** Function: money_rack_input
** Description: Asks the player where they would like to place their 
**				money rack. If a non-integer is entered, the function
**				will ask again, clearing the old input until correct.
**
** Parameters: player, m_rack
**
** Pre-Conditions: 'player' variable must be assigned an integer before
**					function call
** Post-Conditions: m_rack must be returned as an integer
*********************************************************************/
int money_rack_input(int player) {

	int m_rack;

	do {

		if (std::cin.fail()) { // Returns 'true' if input is invalid
			std::cin.clear();
			std::cin.ignore(1000, '\n'); // Ignores up to 1000 characters of text to take new input
		}
		std::cout << "\nPlayer " << player << ", where would you like to place your moneyball rack? Enter 1-5: ";
		std::cin >> m_rack;
		std::cout << std::endl;

	} while (std::cin.fail() || (m_rack < 1 || m_rack > 5));

	m_rack = m_rack - 1; 
	return m_rack;
}



/*********************************************************************
** Function: rack_computer
** Description: Randomly assigns and prints the baseline 5x5 grid to 
**				use when working with regular and moneyballs in the 
**				future. Also returns the points earned by each regular
**				ball.
**
** Parameters:  x, y, player, rack, *regular_points, *money_points
**
** Pre-Conditions: All variables must have been assigned their respective 
**				   data types before calling the function, including
**				   references for regular_points and money_points
**
** Post-Conditions: Explicitly returns money_rack, implicitly returns
**					regular_points and money_points through use of pointers
*********************************************************************/
int rack_computer(int player, char rack[][5], int *regular_points, int *money_points) {
	int x;
	char y;
	*regular_points = 0;

	// Randomly determines whether or not a shot is successful for each member of an array.

	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {

			x = rand() % 2;

			if (x == 1) {

				// X is a miss, O is a successful point, adding one point to the regular score if successful

				rack[i][j] = 'O';
				*regular_points += 1;

			} else {
				rack[i][j] = 'X';
			}
		}
	}

	// Calls money_rack_input to get the location of the money ball rack. money_points is used in here so that
	// it can access the 2D array and get the correct score without hassle
	int money_rack = money_rack_input(player);
	*money_points = money_ball_shots(money_rack, rack);
	return money_rack;
}


/*********************************************************************
** Function: starry_shots
** Description: Calculates the special "starry shots" worth three points
**				each, and displays them after the 5x5 grid of racks.
**
** Parameters: x, starry_array, *starry_points
**
** Pre-Conditions: a char array must be created, and starry_points
**				   must be entered as a reference when calling the function
**
** Post-Conditions: implicitly returns starry_points through use of pointers
*********************************************************************/
void starry_shots(char starry_array[2], int *starry_points) {
	int x;
	*starry_points = 0;

	for (int i = 0; i < 2; i++)
	{
		srand(time(0) + i);
		x = rand() % 2;

		if (x == 1) {

			std::cout << "Starry " << (i + 1) << ": ";
			starry_array[i] = 'W';
			std::cout << starry_array[i] << std::endl;
			*starry_points += 3;

		} else {

			std::cout << "Starry " << (i + 1) << ": ";
			starry_array[i] = 'X';
			std::cout << starry_array[i] << std::endl;
		}
	}
}


/*********************************************************************
** Function: play_game
** Description: Creates most of the arrays and variables needed to play
**				the game, along with calling all the functions required.
**				Includes a callback to self, in order to play again.
**
** Parameters: player_shots, money_rack, starry_array, play_again,
**			   regular_points, money_points, starry_points, player_scores
**
** Pre-Conditions: No pre-conditions other than the function must be called
**
** Post-Conditions: No post-conditions
*********************************************************************/
void play_game() {

	char player_shots[5][5];
	int money_rack;
	char starry_array[2];
	std::string play_again;

	int regular_points;
	int money_points;
	int starry_points;
	int player_scores[2];

	for (int i = 0; i < 2; i++) {

		int player = i + 1;

		// Computes the shots & scores for the current player, returning the money rack for use in score calculating
		money_rack = rack_computer(player, player_shots, &regular_points, &money_points);

		// Computes starry ball scores
		starry_shots(starry_array, &starry_points);

		// Saves the total score for the current player in an array
		player_scores[i] = get_scores(regular_points, money_points, starry_points, money_rack);
	}

	// Determines winner by comparing each player's scores
	if (player_scores[0] > player_scores[1]) {

		std::cout << "\n#### Player 1 wins! ####" << std::endl;

	} else if (player_scores[0] == player_scores[1]) {

		std::cout << "\n#### It's a tie! ####" << std::endl;

	} else {

		std::cout << "\n#### Player 2 wins! ####" << std::endl;
	}

	std::cout << "\nPlay again? (Y/N): ";
	std::cin >> play_again;

	if (play_again == "Y" || play_again == "y" || play_again == "Yes" || play_again == "yes") {

		play_game();
	}
}


/*********************************************************************
** Function: main_menu
** Description: Displays title screen and allows user to learn about
**				the game, play the game, or quit. Slightly over 15 lines
**				in order to fit all menu options and the necessary text 
**				describing how the game is played.
**
** Parameters: menu_input
**
** Pre-Conditions: No pre-conditions other than the function must be called
**
** Post-Conditions: No post-conditions
*********************************************************************/
void main_menu() {

	int menu_input;

	do {

		if (std::cin.fail()) { // Returns 'true' if input is invalid
			std::cin.clear();
			std::cin.ignore(1000, '\n'); // Ignores up to 1000 characters of text to take new input
		}

		std::cout << "\n1. Learn about the game			2. Play the game			3. Exit" << std::endl;
		std::cout << "\nPlease enter a number 1-3: ";
		std::cin >> menu_input;

	} while (std::cin.fail() || (menu_input < 1 || menu_input > 3));

	if (menu_input == 1) {

		std::cout << "\n#######################################################################################" << std::endl;
		std::cout << "\n - Moneyball is a basketball free-throw game, where a player makes throws from 5 racks,\n   attempting to score the most points.\n\n";
		std::cout << " - It gets the name from a special type of ball found in each rack, called the moneyball.\n\n";
		std::cout << " - This ball is worth 2 points, and is found in the fifth position in every rack, along" << std::endl;
		std::cout << "   with a special rack of the player's choosing called the moneyball rack. Along with" << std::endl;
		std::cout << "   the moneyball, there is another special ball on two pedastals called the Starry Ball." << std::endl;;
		std::cout << "\n - This ball, if successfully scored, is worth 3 points." << std::endl;
		std::cout << "\n#######################################################################################" << std::endl;
		main_menu();

	} else if (menu_input == 2) {

		play_game();

	} else if (menu_input == 3) {

		std::cout << "Quitting program..." << std::endl;
		exit(0); // Exits program like normal
	}
}


/*********************************************************************
** Function: main
** Description: The main function. Starts the entire program by calling
**				main_menu().
**
** Parameters: No parameters
**
** Pre-Conditions: No pre-conditions (called automatically)
**
** Post-Conditions: No post-conditions
*********************************************************************/
int main() {
	srand(time(NULL));
	std::cout << "\nWelcome to the Moneyball Game!" << std::endl;
	main_menu();

	return 0;
}
