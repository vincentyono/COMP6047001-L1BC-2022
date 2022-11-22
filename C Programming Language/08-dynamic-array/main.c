#include <stdio.h> // For more information: https://www.ibm.com/docs/en/zos/2.3.0?topic=files-stdioh-standard-input-output
#include <stdlib.h> // For more information: https://www.ibm.com/docs/en/zos/2.3.0?topic=files-stdlibh-standard-library-functions

int main() {

  // malloc

  size_t size = 5;
  int *pm = (int *)malloc(size * sizeof(int)); // dynamically allocated memory

  for (int i = 0; i < size; i++) {
    printf("pm[%d] = %d\n", i, pm[i]); // print some garbage value on the memory
  }

  for (int i = 0; i < size; i++) {
    pm[i] = i + 1;
  }

  printf("\n");

  for (int i = 0; i < size; i++) {
    printf("pm[%d] = %d\n", i, pm[i]);
  }

  printf("\n");

  // calloc

  int *pc = (int *)calloc(size, sizeof(int)); // calloc is similar to malloc
                                              // the difference is that
                                              // calloc initialize the value
                                              // to the allocated memory to 0

  for (int i = 0; i < size; i++) {
    printf("pc[%d] = %d\n", i, pc[i]);
  }

  for (int i = 0; i < size; i++) {
    pc[i] = i + 1;
  }

  printf("\n");

  for (int i = 0; i < size; i++) {
    printf("pc[%d] = %d\n", i, pc[i]);
  }

  printf("\n");

  // realloc

  pc = (int *)realloc(pc, sizeof(int));

  // clang-format off
  for (int i = 0; i < size; i++) {
    printf("pc[%d] = %d\n", i, pc[i]); // pc[1] to pc[4] are equal to some garbage value
  }

  // clang-format on

  // free

  // allocated memory using malloc, calloc or realloc need to be deallocate
  // manually, not deallocating the memory will cause memory leak

  free(pm);
  free(pc);

  return 0;
}