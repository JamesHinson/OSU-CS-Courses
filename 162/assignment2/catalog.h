#include <iostream>
#include <fstream>

using namespace std;

//a struct to hold info of a team
struct Team {
  string name;        //name of the team
  string owner;       //owner of the team
  int market_value;   //market value of the team
  int num_player;     //number of players in the team
  struct Player *p;   //an array that holds all players
  float total_ppg;    //total points per game
};

//a struct to hold info of a player
struct Player {
  string name;      //name of the player
  int age;          //age of the player
  string nation;    //nationality of the player
  float ppg;        //points per game of the player
  float fg;         //field goal percentage
};


/**************************************************
 * Name: create_teams()
 * Description: This function will dynamically allocate
                an array of teams (of the requested size)
 * Parameters: int - size of the array
 * Pre-conditions: none
 * Post-conditions: a Team array of requested size is created and return
 ***********************************************/
Team* create_teams(int);


/**************************************************
 * Name: populate_team_data()
 * Description: This function will fill a single team struct 
                with information that is read in from the file
 * Parameters:  Team* - pointer to the Team array
                int - index of the Team in the array to be filled 
                ifstream& - input file to get information from
 * Pre-conditions: Team array has been allocated; 
                   provided index is less than the array size
 * Post-conditions: a Team at provided index is populated
 ***********************************************/
void populate_team_data(Team*, int, ifstream &); 


/**************************************************
 * Name: create_players()
 * Description: This function will dynamically allocate
                an array of players (of the requested size)
 * Parameters: int - size of the array
 * Pre-conditions: none
 * Post-conditions: a Player array of requested size is created and return
 ***********************************************/
Player* create_players(int);


/**************************************************
 * Name: populate_player_data()
 * Description: This function will fill a single player struct 
                with information that is read in from the file
 * Parameters:  Player* - pointer to the Player array
                int - index of the Player in the array to be filled 
                ifstream& - input file to get information from
 * Pre-conditions: Player array has been allocated; 
                   provided index is less than the array size
 * Post-conditions: a Player at provided index is populated
 ***********************************************/
void populate_player_data(Player*, int, ifstream &); 


/**************************************************
 * Name: delete_info()
 * Description: This function will  delete all the memory that was dynamically allocated
 * Parameters: Team* - the Team array
 * Pre-conditions: the provided Team array hasn't been freed yet
 * Post-conditions: the Team array, with all Players inside, is freed
 ***********************************************/
void delete_info(Team*, int);

/**************************************************
 * Name: input_file()
 * Description: This function will ask the user for a filename to use as input
 * Parameters: none
 * Pre-conditions: none
 * Post-conditions: a filename for use with fstream
 ***********************************************/
ifstream input_file();

/**************************************************
 * Name: menu()
 * Description: This function will allow the user to navigate the program
 * Parameters: Team* - allows display functions to access the available teams array
 *             int - number of teams total
 *             ifstream & - allows access to the file for internal functions
 * Pre-conditions: none
 * Post-conditions: the menu will be printed, and one of the functions will be called based on input,
 *                   either displaying or writing player information to a terminal or file, or quitting the program
 ***********************************************/
void menu(Team*, int, ifstream &);


/**************************************************
 * Name: display_info()
 * Description: This function will allow the user to navigate the program
 * Parameters: none
 * Pre-conditions: none
 * Post-conditions: one of the functions will be called based on input
 ***********************************************/
int display_info();

void search_by_team(Team*, int, int);

void display_top_scorers(Team*, int, int);

void search_by_nation(Team*, int, int);

ofstream write_team_to_file(Team*, int);

void print_team_to_screen(Team*, int);

void print_players_to_screen(Team*, int, int);

void write_players_to_file(Team*, int, int, ofstream &);