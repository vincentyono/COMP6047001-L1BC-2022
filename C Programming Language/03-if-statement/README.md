# 03 - if-statements

## Topic

- math.h
- relational operator
- if-statements
- switch-statements
- ternary operator

### Relational Operators

**Source**: [tutorialspoint](https://www.tutorialspoint.com/cprogramming/c_operators.htm)

| Operator |                                                             Description                                                              |
| :------: | :----------------------------------------------------------------------------------------------------------------------------------: |
|    ==    |                   Checks if the values of two operands are equal or not. If yes, then the condition becomes true.                    |
|    !=    |         Checks if the values of two operands are equal or not. If the values are not equal, then the condition becomes true.         |
|    >     |       Checks if the value of left operand is greater than the value of right operand. If yes, then the condition becomes true.       |
|    <     |        Checks if the value of left operand is less than the value of right operand. If yes, then the condition becomes true.         |
|    >=    | Checks if the value of left operand is greater than or equal to the value of right operand. If yes, then the condition becomes true. |
|    <=    |  Checks if the value of left operand is less than or equal to the value of right operand. If yes, then the condition becomes true.   |

### Logical Operators

| Operator |                                                                        Description                                                                         |
| :------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------: |
|    &&    |                              Called Logical AND operator. If both the operands are non-zero, then the condition becomes true.                              |
|   \|\|   |                            Called Logical OR Operator. If any of the two operands is non-zero, then the condition becomes true.                            |
|    !     | Called Logical NOT Operator. It is used to reverse the logical state of its operand. If a condition is true, then Logical NOT operator will make it false. |

### Assignment Operators

| Operator |                                                             Description                                                             |
| :------: | :---------------------------------------------------------------------------------------------------------------------------------: |
|    =     |                      Simple assignment operator. Assigns values from right side operands to left side operand                       |
|    +=    |        Add AND assignment operator. It adds the right operand to the left operand and assign the result to the left operand.        |
|    -=    | Subtract AND assignment operator. It subtracts the right operand from the left operand and assigns the result to the left operand.  |
|   \*=    | Multiply AND assignment operator. It multiplies the right operand with the left operand and assigns the result to the left operand. |
|    /=    |   Divide AND assignment operator. It divides the left operand with the right operand and assigns the result to the left operand.    |
|    %=    |          Modulus AND assignment operator. It takes modulus using two operands and assigns the result to the left operand.           |
|   <<=    |                                                 Left shift AND assignment operator.                                                 |
|   >>=    |                                                Right shift AND assignment operator.                                                 |
|    &=    |                                                  Bitwise AND assignment operator.                                                   |
|    ^=    |                                            Bitwise exclusive OR and assignment operator.                                            |
|    !=    |                                            Bitwise inclusive OR and assignment operator.                                            |

## Math functions

|                                                    Functions                                                     |                                                                   Description                                                                   |
| :--------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------: |
|          [double acos(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_acos.htm)          |                                                     Returns the arc cosine of x in radians.                                                     |
|          [double asin(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_asin.htm)          |                                                      Returns the arc sine of x in radians.                                                      |
|          [double atan(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_atan.htm)          |                                                    Returns the arc tangent of x in radians.                                                     |
|    [double atan2(double y, double x)](https://www.tutorialspoint.com/c_standard_library/c_function_atan2.htm)    |                 Returns the arc tangent in radians of y/x based on the signs of both values to determine the correct quadrant.                  |
|           [double cos(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_cos.htm)           |                                                     Returns the cosine of a radian angle x.                                                     |
|          [double cosh(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_cosh.htm)          |                                                       Returns the hyperbolic cosine of x.                                                       |
|           [double sin(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_sin.htm)           |                                                      Returns the sine of a radian angle x.                                                      |
|          [double sinh(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_sinh.htm)          |                                                        Returns the hyperbolic sine of x.                                                        |
|          [double tanh(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_tanh.htm)          |                                                      Returns the hyperbolic tangent of x.                                                       |
|           [double exp(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_exp.htm)           |                                                 Returns the value of e raised to the xth power.                                                 |
| [double frexp(double x, int \*exponent)](https://www.tutorialspoint.com/c_standard_library/c_function_frexp.htm) | The returned value is the mantissa and the integer pointed to by exponent is the exponent. The resultant value is x = mantissa \* 2 ^ exponent. |
|  [double ldexp(double x, int exponent)](https://www.tutorialspoint.com/c_standard_library/c_function_ldexp.htm)  |                                           Returns x multiplied by 2 raised to the power of exponent.                                            |
|           [double log(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_log.htm)           |                                             Returns the natural logarithm (base-e logarithm) of x.                                              |
|         [double log10(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_log10.htm)         |                                             Returns the common logarithm (base-10 logarithm) of x.                                              |
| [double modf(double x, double \*integer)](https://www.tutorialspoint.com/c_standard_library/c_function_modf.htm) |                The returned value is the fraction component (part after the decimal), and sets integer to the integer component.                |
|      [double pow(double x, double y)](https://www.tutorialspoint.com/c_standard_library/c_function_pow.htm)      |                                                       Returns x raised to the power of y.                                                       |
|          [double sqrt(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_sqrt.htm)          |                                                          Returns the square root of x.                                                          |
|          [double ceil(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_ceil.htm)          |                                         Returns the smallest integer value greater than or equal to x.                                          |
|          [double fabs(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_fabs.htm)          |                                                        Returns the absolute value of x.                                                         |
|         [double floor(double x)](https://www.tutorialspoint.com/c_standard_library/c_function_fabs.htm)          |                                           Returns the largest integer value less than or equal to x.                                            |
|     [double fmod(double x, double y)](https://www.tutorialspoint.com/c_standard_library/c_function_fmod.htm)     |                                                    Returns the remainder of x divided by y.                                                     |
