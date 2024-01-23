#include <fstream>
#include <iostream>

#include "ex1.h"

using namespace std;

//allocate an array of cars
Car* create_cars(int size){
	return new Car [size];
}

//populate a single car object
void populate_car(Car& c, ifstream& fin){
	fin >> c.brand >> c.num_passenger;
}

//populate the garage object
void populate_garage(Garage& g, ifstream& fin){
	
	//loop through number of cars
	for (int i = 0; i < g.num_cars; ++i)
	{
		populate_car(g.car_arr[i], fin);
	}
}

//print the garage object
void print_garage (Garage& g) {
	
	for (int i = 0; i < g.num_cars; ++i)
	{
		cout << "Brand: " << g.car_arr[i].brand << endl;
		cout << "Num: " << g.car_arr[i].num_passenger << endl;
		cout << endl;
	}
}


//delete function to free memory allocated in g
void delete_garage(Garage& g){
	delete [] g.car_arr;
	g.car_arr = NULL;
}
