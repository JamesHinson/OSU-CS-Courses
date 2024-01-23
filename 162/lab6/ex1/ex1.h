#ifndef EX1_H
#define EX1_H 

using namespace std;

struct Car
{
	string brand;
	int num_passenger;
};

struct Garage
{
	int num_cars; //keep track of the size of the car array
	Car* car_arr;
};

Car* create_cars(int size);
void populate_car (Car& c, ifstream& fin);
void populate_garage(Garage& g, ifstream& fin);
void print_garage(Garage& g);
void delete_garage(Garage& g);



#endif
