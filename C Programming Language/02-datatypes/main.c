#include <limits.h> // For more information: https://www.ibm.com/docs/en/aix/7.2?topic=files-limitsh-file
#include <stdio.h> //  For more information: https://www.ibm.com/docs/en/zos/2.3.0?topic=files-stdioh-standard-input-output

int main() {

  // Data Types

  // char
  char c = 'a'; // Use single quote for char type

  printf("c = %c\n", c); // c = 'a'
  printf("i = %d\n", c); // i = 97

  printf("\n");

  // clang-format off
  printf("size of char type is %d byte\n", sizeof(char)); // 1 byte is equivalent to 8 bits
  printf("char type ranges from %d to %d\n", CHAR_MIN, CHAR_MAX);


  unsigned char uc = '1';

  printf("uc = %d\n", uc); // uc = 49

  printf("\n");
  
  printf("size of unsigned char type is %d bytes\n", sizeof(unsigned char));
  printf("unsigned char type ranges from %d to %d\n", 0, UCHAR_MAX); // unsigned char has no negative values

  printf("\n");

  // char[]

  char str[] = "This is a string"; // string is an array of characters

  printf("%s\n", str);
  printf("size of str type is %d bytes\n", sizeof(str)); // size of char[] is (length of string * sizeof(char)) + 1

  printf("\n");

  // int type

  printf("size of int type is %d bytes\n", sizeof(int));
  printf("size of long int type is %d bytes\n", sizeof(long int));

  printf("\n");

  printf("int type ranges from %d to %d\n", INT_MIN, INT_MAX);
  printf("long int type ranges from %d to %d\n", LONG_MIN, LONG_MAX);

  printf("\n");
  
  // arithmetic operator

  // clang-format on

  int a = 2 - 3 * 2; // C do follow order of operations
  int b = (2 - 3) * 2;

  printf("2 - 3 * 2 = %d\n", a);   // 2 - 3 * 2 = -4
  printf("(2 - 3) * 2 = %d\n", b); // 2 - 3 * 2 = -2

  printf("\n");

  int x1 = 3;
  int y1 = 2;

  printf("%d / %d = %d\n", x1, y1, x1 / y1); // 3 / 2 = 1

  printf("\n");

  float x2 = 3;
  int y2 = 2;

  printf("%.0f / %d = %d\n", x2, y2, x2 / y2);   // 3 / 2 = 0
  printf("%.0f / %d = %.1f\n", x2, y2, x2 / y2); // 3 / 2 = 1.5

  printf("\n");

  // floating-point types

  // pie and pi are PI to 11 decimal places

  float pie = 3.14159265459; // float precision is until 6 decimal places
  double pi = 3.14159265459; // double precision is until 15 decimal places

  printf("pie = %.11f\n", pie); // pie = 3.14159274101
  printf("pi = %.11lf\n", pi);  // pi = 3.14159265459

  printf("\n");

  // Bitwise operator

  unsigned char p = 3, q = 2, r = 255;

  unsigned char and = p & q;
  unsigned char or = p | q;
  unsigned char xor = p ^ q;
  unsigned char not = ~r;
  unsigned char ls = q << 1;
  unsigned char rs = q >> 1;

  // clang-format off

  printf("p & q = %d\n", and); // p = 0000 0011
                               // q = 0000 0010
                               // --------------
                           // p & q = 0000 0010 = 2

  printf("p | q = %d\n", or); // p = 0000 0011
                              // q = 0000 0010
                              // --------------
                          // p | q = 0000 0011 = 3

  printf("p ^ q = %d\n", xor); // p = 0000 0011
                               // q = 0000 0010
                               // --------------
                           // p ^ q = 0000 0001 = 1

  printf("~r = %d\n", not); // r = 1111 1111
                            // --------------
                           // ~r = 0000 0000 = 0

  printf("q << 1 = %d\n", ls); // q = 0000 0010
                               // --------------
                          // q << 1 = 0000 0100 = 4

  printf("q >> 1 = %d\n", rs); // q = 0000 0010
                               // --------------
                          // q >> 1 = 0000 0001 = 1

  return 0;
}