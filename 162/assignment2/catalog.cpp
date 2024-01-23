#include "catalog.h"

using namespace std;

//function definitions go here
Team* create_teams(int num) { // num = number of teams - first line in text file
	Team *teams = new Team[num];
	return teams;
}



Player* create_players(int num) { // num = number of players for each team - end of team info line
	Player *players = new Player[num];
	return players;
}



void delete_info(Team *teams, int num_teams) {
	for (int i = 0; i < num_teams; i++)
	{
		delete [] teams[i].p; // segmentation fault occurs here
		teams[i].p = nullptr;
	}
	delete [] teams;
	teams = nullptr;
}



void populate_player_data(Player *player, int index, ifstream &my_file) {
	my_file >> player[index].name;
	my_file >> player[index].age;
	my_file >> player[index].nation;
	my_file >> player[index].ppg;
	my_file >> player[index].fg;
}


/**************************************************
 * Serves multiple purposes: adds the total ppg, cycles through the
 * current team's players to prepare to populate the next team's struct,
 * and populates the player data for each player in the current team.
 **************************************************/
void populate_team_data(Team *team, int index, ifstream &my_file) { // index = the team to be filled in the teams array
	string word;
	my_file >> team[index].name;
	my_file >> team[index].owner;
	my_file >> team[index].market_value;
	my_file >> team[index].num_player;
	team[index].p = create_players(team[index].num_player);
	team[index].total_ppg = 0;

	for (int i = 0; i < team[index].num_player; i++)
	{									 			
		populate_player_data(team[index].p, i, my_file); 
		team[index].total_ppg += team[index].p[i].ppg;
		getline(my_file, word);
	}
}



ifstream input_file() { // asks for file; if file is invalid, ask again

	ifstream my_file;
	string file_name;

	cout << "\nEnter the team info file name: ";
	cin >> file_name;
	cout << endl;

	my_file.open(file_name);

	if (!my_file)
	{
		do {
			cout << "That file doesn't exist or is invalid, please enter a valid .txt file." << endl;
			cout << "Enter the team info file name: ";
			cin >> file_name;
			cout << endl;

			my_file.open(file_name);

		} while (!my_file);
	}

	cout << "File " << file_name << " opened successfully" << endl;
	cout << endl;

	return my_file;
}



void menu(Team *teams, int num_teams, ifstream &my_file) {
	int menu_input;
	int display_type;

	cout << "1. Search team by its name" << endl;
	cout << "2. Display the top scorer of each team" << endl;
	cout << "3. Search players by nationality" << endl;
	cout << "4. Quit" << std::endl;
	cout << "\nYour choice: ";
	cin >> menu_input;
	cout << endl;

	if (cin.fail() || (menu_input < 1 || menu_input > 4)) // Returns 'true' if input is invalid
	{
		cin.clear();
		cin.ignore(1000, '\n'); // Ignores up to 1000 characters of text to take new input
	
		do {
			cout << "That's not a valid input." << endl;
			cout << "\nPlease enter a number between 1 and 4: ";
			cin >> menu_input;
			cout << endl;

		} while (cin.fail() || (menu_input < 1 || menu_input > 4));
	}

	if (menu_input == 1)
	{
		display_type = display_info();
		search_by_team(teams, display_type, num_teams);

	} else if (menu_input == 2)
	{
		display_type = display_info();
	//	display_top_scorers(teams, display_type, num_teams);

	} else if (menu_input == 3)
	{
		display_type = display_info();
	//	search_by_nation(teams, display_type, num_teams);

	} else if (menu_input == 4)
	{
		cout << "Quitting program..." << std::endl;
		exit(0); // Exits program like normal
	}
}



int display_info() {
	int menu_input;

	do {

		if (cin.fail()) { // Returns 'true' if input is invalid
			cin.clear();
			cin.ignore(1000, '\n'); // Ignores up to 1000 characters of text to take new input
		}

		cout << "How would you like the information displayed?" << endl;
		cout << "1. Print to screen (Press 1)" << endl;
		cout << "2. Print to file (Press 2)" << endl;
		cout << "\nYour choice: ";
		cin >> menu_input;
		cout << endl;

	} while (cin.fail() || (menu_input < 1 || menu_input > 2));

	return menu_input;
}



void search_by_team(Team *teams, int display_type, int num_teams) {

	string team_to_print;
	ofstream output_file;

	cout << "Enter the team's name: ";
	cin >> team_to_print;
	cout << endl;

	if (display_type == 1)
	{
		for (int i = 0; i < num_teams; i++)
		{
			if (teams[i].name == team_to_print)
			{
				print_team_to_screen(teams, i);
				print_players_to_screen(teams, i, num_teams);
			} else if (i == num_teams && (teams[i].name != team_to_print))
			{
				cout << "That is an invalid team name. Please ensure the name is spelled correctly." << endl;
				search_by_team(teams, display_type, num_teams);
			}
		}
	} else if (display_type == 2)
	{
		for (int i = 0; i < num_teams; i++)
		{
			if (teams[i].name == team_to_print)
			{
				output_file = write_team_to_file(teams, i);
				write_players_to_file(teams, i, num_teams, output_file);
			} else if (i == num_teams && (teams[i].name != team_to_print))
			{
				cout << "That is an invalid team name. Please ensure the name is spelled correctly." << endl;
				search_by_team(teams, display_type, num_teams);
			}
		}
	}
}



void print_team_to_screen(Team *teams, int team_to_print) {
	cout << "############################################\n" << endl;
	cout << "Team name: " << teams[team_to_print].name << endl;
	cout << "Team owner: " << teams[team_to_print].owner << endl;
	cout << "Team Market Value: " << teams[team_to_print].market_value << endl;
	cout << "Number of players: " << teams[team_to_print].num_player << endl;
	cout << "Total points per game: " << teams[team_to_print].total_ppg << endl;
	cout << "\n############################################\n" << endl;
}



ofstream write_team_to_file(Team *teams, int team_to_print) {
	ofstream output_file;
	string write_file;

	cout << "Please provide the filename to write to, including .txt: ";
	cin >> write_file;

	output_file.open(write_file, ios::app);

	output_file << "############################################" << endl;
	output_file << "Team name: " << teams[team_to_print].name << endl;
	output_file << "Team owner: " << teams[team_to_print].owner << endl;
	output_file << "Team Market Value: " << teams[team_to_print].market_value << endl;
	output_file << "Number of players: " << teams[team_to_print].num_player << endl;
	output_file << "Total points per game: " << teams[team_to_print].total_ppg << endl;
	output_file << "\n############################################" << endl;

	return output_file;
}



void print_players_to_screen(Team *teams, int team, int num_player) {

	cout << "Players:\n" << endl;
	// cout << "--------------------------------------------\n" << endl;

	for (int i = 0; i < num_player; i++)
	{
		cout << "Name: " << teams[team].p[i].name << endl;
		cout << "Age: " << teams[team].p[i].age << endl;
		cout << "Nationality: " << teams[team].p[i].nation << endl;
		cout << "Points Per Game: " << teams[team].p[i].ppg << endl;
		cout << "Field Goal Percentage: " << teams[team].p[i].fg << endl;
		cout << endl;
		// cout << "--------------------------------------------" << endl;
	}
}



void write_players_to_file(Team *teams, int team, int num_player, ofstream &output_file) {

	output_file << "Players:\n" << endl;
	// output_file << "--------------------------------------------\n" << endl;

	for (int i = 0; i < num_player; i++)
	{
		output_file << "Name: " << teams[team].p[i].name << endl;
		output_file << "Age: " << teams[team].p[i].age << endl;
		output_file << "Nationality: " << teams[team].p[i].nation << endl;
		output_file << "Points Per Game: " << teams[team].p[i].ppg << endl;
		output_file << "Field Goal Percentage: " << teams[team].p[i].fg << endl;		
		output_file << endl;
		// output_file << "--------------------------------------------" << endl;
	}
}