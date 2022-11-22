#include <stdio.h> // For more information: https://www.ibm.com/docs/en/zos/2.3.0?topic=files-stdioh-standard-input-output

int main() {
  // for-loops

  printf("----------\n");
  printf("for loop\n");
  printf("\n");

  // clang-format off
  // the format of for loops usually is:
  // for([declaring and initializing variable]; [conditional]; incrementing variables)
  // clang-format on

  for (int i = 0; i < 10; i++) {
    printf("i = %d\n", i);
  }

  // You can also omit something you don't need
  // the for loop below will result in infinite loops

  int i = 0;

  // for (;; i++) {
  //   printf("i = %d\n", i);
  // }

  printf("\n");
  printf("----------\n");
  printf("while loop - 1\n");
  printf("\n");

  // While loop

  i = 0;

  // It will keep looping until the conditional return false;
  while (i < 10) {
    printf("i = %d\n", i++); // increment i by 1, after
  }

  printf("\n");
  printf("----------\n");
  printf("while loop - 2\n");
  printf("\n");

  i = 0;

  // It will keep looping until the conditional return false;
  while (i < 10) {
    printf("i = %d\n", ++i); // increment i by 1, before
  }

  // do while loop

  // The difference between do while loop and while loop:
  // do while loop, loop at least one time (if the initial condition is false)
  // while, while loop won't loop if the initiaal condition is false

  i = 0;

  printf("\n");
  printf("----------\n");
  printf("Do while loop\n");
  printf("\n");

  do {
    printf("i = %d\n", i++); // increment i by 1, after
  } while (i < 10);

  printf("\n");
  return 0;
}