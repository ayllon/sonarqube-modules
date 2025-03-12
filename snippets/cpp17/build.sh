# These two can be done in parallel
clang++ -std=c++17 -c -o library.o library.cpp
clang++ -std=c++17 -c -o main.o main.cpp

clang++ -std=c++17 -o main main.o library.o
./main
