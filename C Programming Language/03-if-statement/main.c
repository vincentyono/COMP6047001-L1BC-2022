#include <math.h> // For more information: https://www.ibm.com/docs/en/zos/2.3.0?topic=files-mathh-floating-point-math-functions
#include <stdbool.h> //For more information: https://www.ibm.com/docs/en/zos/2.1.0?topic=files-stdboolh
#include <stdio.h> // For more information: https://www.ibm.com/docs/en/zos/2.3.0?topic=files-stdioh-standard-input-output
#include <string.h> // For more information: https://www.ibm.com/docs/en/i/7.4?topic=files-stringh

int main() {

  // math.h

  // Here are the full list of functions:
  // https://www.ibm.com/docs/en/zos/2.3.0?topic=files-mathh-floating-point-math-functions

  // clang-format off
  printf("sqrt(9) = %.0f\n", sqrt(9)); // square root, Output: sqrt(9) = 3
  printf("cbrt(27) = %.0f\n", cbrt(27)); // cube root, Output: cbrt(27) = 3
  printf("pow(2, 4) = %.0f\n", pow(2, 4)); // power function the first argument is the base
                                           // and raise to the second argument, Output: pow(2, 4) = 16
  printf("log(2) = %f\n", log(2)); // logarithm, Output: log(2) = 0.693147

  printf("round(3.14) = %d\n", (int)round(3.14)); // round number, Output: round(3.14) = 3
  printf("ceil(1.0001) = %d\n", (int)ceil(1.0001)); // round up number, Output: ceil(1.0001) = 2
  printf("floor(1.99) = %d\n", (int)floor(1.99)); // round down number, Output: floor(1.99) = 1
  
  printf("fabs(-100) = %lf\n", fabs(-100)); // absolute value, Output: fabs(-100) = 100

  printf("sin(45) = %f\n", sin(45)); // Output: sin(45) = 0.850904
  printf("cos(45) = %f\n", cos(45)); // Output: cos(45) = 0.525322
  printf("tan(45) = %f\n", tan(45)); // Output: tan(45) = 1.619775

  printf("\n");

  // relational operator

  int burger = 10, soda = 5, pizza = 15;

  bool a = pizza == (burger + soda); // Output: 1
  bool b = burger > pizza; // Output: 0
  bool c = burger < pizza; // Output: 1
  bool d = pizza >= (burger + soda); // Output: 1
  bool e = burger <= soda; // Output: 0

  printf("pizza == (burger + soda) = %d\n", a);
  printf("burger > pizza = %d\n", b);
  printf("burger < pizza = %d\n", c);
  printf("pizza >= (burger + soda) = %d\n", d);
  printf("burger <= soda = %d\n", e);

  printf("\n");

  // if-statements
  // clang-format on

  int score = 70;
  char grade;

  printf("Your score: %d\n", score);

  if (score > 85) {
    grade = 'A';
    printf("You got an A\n");
  } else if (score > 75) {
    grade = 'B';
    printf("You got a B\n");
  } else if (score > 65) {
    grade = 'C';
    printf("You got a C\n");
  } else if (score > 50) {
    grade = 'D';
    printf("You got a D\n");
  } else {
    grade = 'F';
    printf("You got an F\n");
  }

  // switch-statement

  switch (grade) {
  case 'A': // expression must be a constant value
    printf("Perfect!\n");
    break; // don't forget to put break in between each case,
           // or it will cause it to,
           // execute all code from the true case to the last.
  case 'B':
    printf("Good!\n");
    break;
  case 'C':
    printf("Average\n");
    break;
  case 'D':
    printf("Poor\n");
    break;
  case 'F':
    printf("Fail\n");
    break;
  default:
    printf("Invalid grade\n");
  }

  // ternary operator

  // clang-format off
  printf("%s\n", grade != 'F' ? "Pass" : "Fail"); // Format: [Conditional] ? [if true] : [if false];

  // string comparison

  printf("\n");

  char str1[] = "String", str2[] = "String";
  bool f = "String" == "String";
  bool g = str1 == str2;
  bool h = strcmp(str1, str2) == 0; // strcmp return 0 if strings are equal, 
                                    // https://www.programiz.com/c-programming/library-function/string.h/strcmp

  printf("\"String\" == \"String\" = %d\n", f); // Output: 1
  printf("str1 == str2 = %d\n", g); // Output: 0
  printf("strcmp(str1, str2) = %d\n", h); // Output: 1

  return 0;
}