CC=g++ -std=c++11 -g
exe=stairs

$(exe): recurse.o stairs.o
	$(CC) recurse.o stairs.o -o $(exe)

recurse.o: recurse.cpp
	$(CC) recurse.cpp -c

stairs.o: stairs.cpp
	$(CC) stairs.cpp -c