#include "Addition/addition.h"
#include "Subtraction/subtraction.h"
#include <stdio.h>

int main() {
  double a = 5, b = 3;

  printf("%.0lf + %.0lf = %.0lf\n", a, b, addition(a, b));
  printf("%.0lf - %.0lf = %.0lf\n", a, b, subtraction(a, b));

  return 0;
}
