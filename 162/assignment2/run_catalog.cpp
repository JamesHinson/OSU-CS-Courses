#include <iostream>
#include <fstream>
#include "catalog.h"

using namespace std;

int main()
{
	ifstream myfile = input_file(); // gets the file to input to from the user

	int num_teams;
	myfile >> num_teams;

	Team *teams;
	teams = create_teams(num_teams); // creates a dynamic array of all teams in the file
	
	for (int i = 0; i < num_teams; i++)
	{
		populate_team_data(teams, i, myfile); // populates player & team data for each team in the file
	}

	menu(teams, num_teams, myfile); // runs the main menu; uses teams, num_teams, and myfile 
									// for internal function calls that require specific data

	delete_info(teams, num_teams); // frees the allocated memory from each team and player within that team

	return 0;
}