CC=g++ -std=c++11 -g
exe=linked_list

$(exe): linked_list.o test_linked_list.o
	$(CC) linked_list.o test_linked_list.o -o $(exe)

linked_list.o: linked_list.cpp
	$(CC) linked_list.cpp -c

test_linked_list.o: test_linked_list.cpp
	$(CC) test_linked_list.cpp -c