# Now these have to be done in order
clang++ -std=c++20 -c library.cppm -o library.o -fmodule-output=library.pcm
clang++ -std=c++20 -c main.cpp -o main.o -fmodule-file=library=library.pcm

clang++ -std=c++20 main.o library.o -o main
./main
