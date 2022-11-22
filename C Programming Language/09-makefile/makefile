all: main

main: addition.o subtraction.o
	gcc addition.o subtraction.o main.c -o main

addition.o:
	gcc -c ./Addition/addition.c -o addition.o

subtraction.o:
	gcc -c ./Subtraction/subtraction.c -o subtraction.o

clean:
	rm *.o main.exe