coffee_shop: main.o order.o menu.o coffee.o shop.o
	g++ -Wall main.o order.o menu.o coffee.o shop.o -o coffee_shop

# Double check how to compile a driver file!
main.o: main.cpp shop.h menu.h
	g++ -c main.cpp

shop.o: shop.cpp shop.h
	g++ -c shop.cpp

order.o: order.cpp order.h
	g++ -c order.cpp

menu.o: menu.cpp menu.h
	g++ -c menu.cpp

coffee.o: coffee.cpp coffee.h
	g++ -c coffee.cpp