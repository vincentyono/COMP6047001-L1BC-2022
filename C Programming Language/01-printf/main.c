#include <stdio.h> // For more information: https://www.ibm.com/docs/en/zos/2.3.0?topic=files-stdioh-standard-input-output
/*

 Every C program need to have main function,
 if you are curious about using int and return 0 in the main function here is
 a link you can read:
 https://www.tutorialspoint.com/difference-between-void-main-and-int-main-in-c-cplusplus#:~:text=The%20void%20main()%20indicates,use%20the%20void%20main().

*/

int main() {
  // clang-format off
  // Hello World!
  printf("Hello World!\n"); // printf function prints a string to the console,
                         // NOTE: unlike in python, it won't add newline by
                         // default
                         //
                         // Example:
                         // printf("Hello World");
                         // printf("Hello World");
                         // printf("Hello World");
                         // printf("Hello World");
                         //
                         // Output: Hello WorldHello WorldHello WorldHello World
  // Variables

  // When declaring a variable, we need to specify the data type

  int a; // declaration
  a = 0; // initialization

  int b = 0; // declaration + initialization

  int one = 1, two = 2, three = 3, four = 4, five = 5; // same data type can be declared and initialize in one line

  // constant

  
  const float PI = 3.141592654; // we can't modify the value of constant,
                                // the convention is to use All Capital letters for constant

  // PI = 420.69; <- this will be an error

  /*

    NOTE: you can't declare a variable with the same variable name as other
    variable.

    Example:

    int a = 0;
    int a = 1; // this will result in an error,

    NOTE: It may only give you an error during compile time

  */
  /*

    Escape sequences

    there are a lot of different escape sequences
    You can read from the following Documentation:
    https://www.ibm.com/docs/en/rdfi/9.6.0?topic=set-escape-sequences


    \n - Newline
    \t - Tab
    \\ - backslash
    \' = Single quotation mark
    \" - Double quotation mark

  */

  printf("Newline\nNewline\n");
  printf("Tab\tTab\n");
  printf("C:\\Users\\username\\Desktop\n");
  printf("%c\n", '\'');
  printf("\"If at first you don't suceed, then skydiving definitely isn't for you.\" Steven Wright\n");

  /*

    Output:

    Newline
    Newline
    Tab     Tab
    C:\Users\username\Desktop
    '
    "If at first you don't suceed, then skydiving definitely isn't for you." Steven Wright

  */

  return 0;
}
