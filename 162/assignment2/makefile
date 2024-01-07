run_catalog: run_catalog.o catalog.o
	g++ run_catalog.o catalog.o -o run_catalog

run_catalog.o: run_catalog.cpp catalog.h
	g++ -c run_catalog.cpp

catalog.o: catalog.cpp catalog.h
	g++ -c catalog.cpp