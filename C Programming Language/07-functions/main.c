#include "division.h"

#include <stdio.h> // For more information: https://www.ibm.com/docs/en/zos/2.3.0?topic=files-stdioh-standard-input-output
#include <string.h> // For more information: https://www.ibm.com/docs/en/i/7.4?topic=files-stringh

int subtraction(int a, int b) { return a - b; }

int multiplication(int a, int b); // this is a function prototype
void print_address(int a);
void increment(int *a);
// clang-format on

int fail_sum(int arr[]) {
  int length = sizeof(arr) / sizeof(arr[0]);
  int sum = 0;

  printf("(fail_sum) the size of arr = %d bytes\n", sizeof(arr));
  printf("(fail_sum) the length of arr = %d\n", length);

  for (int i = 0; i < length; i++) {
    sum += arr[i];
  }

  return sum;
}

int sum(int arr[], int length) {
  int sum = 0;

  for (int i = 0; i < length; i++) {
    sum += arr[i];
  }

  return sum;
}

int main() {
  // clang-format off
  int a = 12, b = 34;

  //   printf("%d + %d = %d\n", a, b, addition(a, b)); // Output: 12 + 34 = 46
  //   printf("addition(%d) = %d\n", a, addition(a)); // There are no error on compile time

  printf("%d - %d = %d\n", a, b, substraction(a, b)); // Output: 12 - 32 = -22
  //   printf("substraction(%d)\n", a, substraction(a)); // This will give error on compile time

  printf("%d * %d = %d\n", a, b, multiplication(a, b)); // Output: 12 * 34 = 408
  //   printf("multiplication(%d) = %d\n", a, b, multiplication(a)); // This will give error on compile time

  printf("%d / %d = %d\n", b, a, division(b, a)); // Output: 34 / 12 = 2

  // The address of variables from main and variables from function are different
  printf("(main) Address of a = %p\n", &a);
  print_address(a);

  increment(&a);
  printf("a = %d\n", a);

  printf("\n");
  
  // accessing array from functions

  // clang-format on
  int arr[] = {1, 2, 3, 4, 5};
  int length = sizeof(arr) / sizeof(arr[0]);

  printf("(main) the size of arr = %d bytes\n", sizeof(arr));
  printf("(main) the length of arr = %d\n", length);

  printf("\n");

  printf("fail_sum = %d\n", fail_sum(arr));
  printf("sum = %d\n", sum(arr, length));

  return 0;
}

// to declare a function you need to specify the function's return type
int addition(int a, int b) { return a + b; }
int multiplication(int a, int b) { return a * b; }
void increment(int *a) { *a = (*a) + 1; }
void print_address(int a) { printf("(print_address) Address of a = %p\n", &a); }
