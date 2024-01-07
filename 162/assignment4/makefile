CC=g++ -std=c++11 -g
exe=asm4

# Complete the makefile
# Your code here: 
$(exe): main.o game.o room.o event.o bats.o gold.o stalactites.o wumpus.o
	$(CC) main.o game.o room.o event.o bats.o gold.o stalactites.o wumpus.o -o asm4

main.o: main.cpp
	$(CC) main.cpp -c

game.o: game.cpp
	$(CC) game.cpp -c

room.o: room.cpp
	$(CC) room.cpp -c

event.o: event.cpp
	$(CC) event.cpp -c

bats.o: bats.cpp
	$(CC) bats.cpp -c

gold.o: gold.cpp
	$(CC) gold.cpp -c

stalactites.o: stalactites.cpp
	$(CC) stalactites.cpp -c

wumpus.o: wumpus.cpp
	$(CC) wumpus.cpp -c
