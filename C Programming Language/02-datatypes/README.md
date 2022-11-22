# 02 - datatypes

## Topic

- data types
- arithmetic operator
- bitwise operator

**Source**: [Wikipedia](https://en.wikipedia.org/wiki/C_data_types), [tutorialspoint](https://www.tutorialspoint.com/cprogramming/c_data_types.htm)

## Integer Types

| Type                                                             | Storage size (bytes) |         Format specifier          | Range (limit.h variable) |                          Range                          | Suffix for decimal constants |
| :--------------------------------------------------------------- | :------------------: | :-------------------------------: | :----------------------: | :-----------------------------------------------------: | :--------------------------: |
| char                                                             |          1           |                %c                 |   CHAR_MIN to CHAR_MAX   |                 -128 to 127 or 0 to 255                 |             n/a              |
| signed char                                                      |          1           | %c (or %hhi for numerical output) |  SCHAR_MIN to SCHAR_MAX  |                       -128 to 127                       |             n/a              |
| unsigned char                                                    |          1           | %c (or %hhu for numerical output) |      0 to UCHAR_MAX      |                        0 to 255                         |             n/a              |
| short, short int, signed short, signed short int                 |          2           |            %hi or %hd             |   SHRT_MIN to SHRT_MAX   |                    -32,768 to 32,767                    |             n/a              |
| unsigned short, unsigned short int                               |          2           |                %hu                |      0 to USHRT_MAX      |                       0 to 65,535                       |             n/a              |
| int, signed, signed int                                          |        2 or 4        |             %i or %d              |    INT_MIN to INT_MAX    |  -32,768 to 32,767 or -2,147,483,648 to 2,147,483,647   |             n/a              |
| unsigned, unsigned int                                           |        2 or 4        |                %u                 |      0 to UINT_MAX       |            0 to 65,535 or 0 to 4,294,967,295            |            u or U            |
| long, long int, signed long, signed long int                     |          4           |            %li or %ld             |   LONG_MIN to LONG_MAX   |             -2,147,483,648 to 2,147,483,647             |            l or L            |
| unsigned long, unsigned long int                                 |          4           |                %lu                |      0 to ULONG_MAX      |                   0 to 4,294,967,295                    |    both u or U and l or L    |
| long long, long long int, signed long long, signed long long int |          8           |           %lli or %lld            |  LLONG_MIN to LLONG_MAX  | −9,223,372,036,854,775,807 to 9,223,372,036,854,775,807 |           ll or LL           |
| unsigned long long, unsigned long long int                       |          8           |               %llu                |     0 to ULLONG_MAX      |             0 to 18,446,744,073,709,551,615             |   both u or U and ll or LL   |

## Floating-Point Types

| Type        | Storage size (bytes) |            Format specifier            |         Range          |     Precision     | Suffix for decimal constants |
| :---------- | :------------------: | :------------------------------------: | :--------------------: | :---------------: | :--------------------------: |
| float       |          4           |     %f, %F, %g, %G, %e,%E, %a, %A      |   1.2E-38 to 3.4E+38   | 6 decimal places  |            f or F            |
| double      |          8           | %lf, %lF, %lg, %lG, %le, %lE, %la, %lA |  2.3E-308 to 1.7E+308  | 15 decimal places |             n/a              |
| long double |          16          | %Lf, %LF, %Lg, %LG, %Le, %LE, %La, %LA | 3.4E-4932 to 1.1E+4932 | 19 decimal places |            l or L            |

## Operator

### Arithmetic Operator

| Operator |                      Description                       |
| :------: | :----------------------------------------------------: |
|    +     |                   Adds two operands.                   |
|    -     |        Subtracts second operand from the first.        |
|    \*    |               Multiplies both operands.                |
|    /     |           Divides numerator by de-numerator.           |
|    ++    | Increment operator increases the integer value by one. |
|    --    | Decrement operator decreases the integer value by one. |

### Bitwise Operator

| Operator |                                                        Description                                                        |
| :------: | :-----------------------------------------------------------------------------------------------------------------------: |
|    &     |                       Binary AND Operator copies a bit to the result if it exists in both operands.                       |
|    \|    |                              Binary OR Operator copies a bit if it exists in either operand.                              |
|    ^     |                       Binary XOR Operator copies the bit if it is set in one operand but not both.                        |
|    ~     |                     Binary One's Complement Operator is unary and has the effect of 'flipping' bits.                      |
|    <<    |  Binary Left Shift Operator. The left operands value is moved left by the number of bits specified by the right operand.  |
|    >>    | Binary Right Shift Operator. The left operands value is moved right by the number of bits specified by the right operand. |

### Truth table for AND operation

|  a  |  b  | a AND b |
| :-: | :-: | :-----: |
|  0  |  0  |    0    |
|  0  |  1  |    0    |
|  1  |  0  |    0    |
|  1  |  1  |    1    |

### Truth table for OR operation

|  a  |  b  | a OR b |
| :-: | :-: | :----: |
|  0  |  0  |   0    |
|  0  |  1  |   1    |
|  1  |  0  |   1    |
|  1  |  1  |   1    |

### Truth table for XOR operation

|  a  |  b  | a XOR b |
| :-: | :-: | :-----: |
|  0  |  0  |    0    |
|  0  |  1  |    1    |
|  1  |  0  |    1    |
|  1  |  1  |    0    |

### Truth table for NOT operation

|  a  | NOT a |
| :-: | :---: |
|  0  |   1   |
|  1  |   0   |

## ASCII Table

![image](https://bournetocode.com/projects/GCSE_Computing_Fundamentals/pages/img/ascii_table_lge.png)
