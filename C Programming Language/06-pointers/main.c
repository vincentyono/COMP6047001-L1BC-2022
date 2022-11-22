#include <stdio.h> // For more information: https://www.ibm.com/docs/en/zos/2.3.0?topic=files-stdioh-standard-input-output
#include <string.h> // For more information: https://www.ibm.com/docs/en/i/7.4?topic=files-stringh

int main() {
  // pointers

  int a = 10;
  int *p = &a; // p is a pointer to a
               // using * to indicate variable p is a pointer of type int
               // using & to reference variable a

  printf("&a = %p\n", &a); // &a is the address of variable a
  printf("p = %p\n", p);   // format specifier for pointer is %p

  printf("*p = %d\n", *p); // use * to output the value that is being pointed
  printf("*p = %p\n", &p); // pointer also has an address

  // pointers arithmetic

  // clang-format off

  printf("Address of p = %lld\n", p);             // because the size of int is 4 bytes
  printf("Address of (p + 1) = %lld\n", p + 1);   // the value of p + 1 is 4 more than p
  
  long double b = 1.326571894743281095;
  long double *pb = &b;

  printf("Address of pb = %lld\n", pb);             // because the size of long double is 16 bytes
  printf("Address of (pb + 1) = %lld\n", pb + 1);   // the value of pb + 1 is 16 more than pb

  printf("\n");

  // clang-format on

  // array

  int numbers[] = {12, 24, 36, 48, 60};

  // clang-format off
  printf("numbers = %p\n", numbers); // numbers is an address pointing to the
                                     // first index of the array

  printf("\n");

  printf("*numbers = %d\n", *numbers);             // Output: *numbers = 12
  printf("*(numbers + 1) = %d\n", *(numbers + 1)); // Output: *(numbers + 1) = 24
  printf("*(numbers + 2) = %d\n", *(numbers + 2)); // Output: *(numbers + 1) = 36
  printf("*(numbers + 3) = %d\n", *(numbers + 3)); // Output: *(numbers + 1) = 48
  printf("*(numbers + 4) = %d\n", *(numbers + 4)); // Output: *(numbers + 1) = 60
  
  printf("\n");

  printf("numbers[0] = %d\n", numbers[0]); // Output: number[0] = 12 
  printf("numbers[1] = %d\n", numbers[1]); // Output: number[1] = 24
  printf("numbers[2] = %d\n", numbers[2]); // Output: number[2] = 36
  printf("numbers[3] = %d\n", numbers[3]); // Output: number[3] = 48
  printf("numbers[4] = %d\n", numbers[4]); // Output: number[4] = 60

  int length = sizeof(numbers)/sizeof(numbers[0]); // length of array
                                                   // sizeof(numbers) = 20, because int is 4 bytes 
                                                   // and it has 5 elements in the array (5 * 4 bytes = 20 bytes)
                                                   // sizeof(numbers[0]) = 4, because an int is 4 bytes
                                                   // sizeof(numbers)/sizeof(numbers[0]) = 5

  printf("length of numbers = %d\n", length);

  printf("\n");
  
  // char array

//   char food[6];
  char food[7];

  food[0] = 'B';
  food[1] = 'U';
  food[2] = 'R';
  food[3] = 'G';
  food[4] = 'E';
  food[5] = 'R';
  food[6] = '\0';   // every char array need to have \0 (NULL) to indicate the end of the string

  printf("food = %s\n", food);

  char drink[] = "SODA"; // C Compiler will put extra \0 (NULL) characters at the end of the string by default

  for(unsigned i = 0; i < sizeof(drink)/sizeof(drink[0]); i++) { // since the size of drink is 5 bytes, sizeof(drink)/sizeof(drink[0]) = 5
    printf("drink[%d] = %c\n", i, drink[i]); // drink[4] = '\0' which is NULL
  }
  
  printf("\n");

  for(unsigned i = 0; i < strlen(drink); i++) { // strlen(drink) = 4
    printf("drink[%d] = %c\n", i, drink[i]); // drink[4] = '\0' which is NULL
  }

  printf("\n");

  // 2D - array

  int arr[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

  printf("size of arr[0][0] = %d bytes\n", sizeof(arr[0][0])); // the size of arr[0][0] = 4 bytes (int type is 4 bytes)
  printf("size of arr[0] = %d bytes\n", sizeof(arr[0])); // the size of arr[0] = 12 bytes (arr[0] contain 3 int, so the size of arr[0] = 3 * 4 bytes)
  printf("size of arr = %d bytes\n", sizeof(arr)); // the size of arr = 36 bytes (arr contain 3 array of length 3, so the size of arr = 3 * (3 * 4) bytes)

  printf("\n");

  // generally used formula for length of array: sizeof([array]) / sizeof([first index of the array])

  for (unsigned i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
    for (unsigned j = 0; j < sizeof(arr[0]) / sizeof(arr[0][0]); j++) {
      printf("arr[%d][%d] = %d\n", i, j, arr[i][j]);
    }
    printf("\n");
  }

  printf("\n");

  for (unsigned i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
    for (unsigned j = 0; j < sizeof(arr[0]) / sizeof(arr[0][0]); j++) {
      printf("*(*(arr + %d) + %d) = %d\n", i, j, *(*(arr + i) + j)); // This is another way to iterate 2D array
    }                                                                // using pointers arithmetic
    printf("\n");
  }

  return 0;
}