#include <stdio.h> // For more information: https://www.ibm.com/docs/en/zos/2.3.0?topic=files-stdioh-standard-input-output
#include <string.h> // For more information: https://www.ibm.com/docs/en/i/7.4?topic=files-stringh

int main() {
  // clang-format off

  // fgets and scanf

  char quote[50]; // char username[50] can receive string with the maximum
                      // length of 50 characters

  char username[20];
  char year[5];
  
  printf("Enter a quote: ");
  
//   scanf("%s", &fullname); // the second argument need to have & in front of the
                             // variable name. putting & in front of the variable name
                             // return the address of the variable instead of value
  
  fgets(quote, 50, stdin); // unlike scanf fgets can accept whitespaces
                              // but it put newline in the end
  
  quote[strlen(quote) - 1] = '\0'; // removes newline

  printf("Enter username: ");
  // scanf("%s", &username);

  fgets(username, 25, stdin);
  
  username[strlen(username) - 1] = '\0'; // removes newline

  printf("Enter year: ");
  fgets(year, 5, stdin);

  printf("\n");

  // clang-format on
  printf("\"%s\" - %s, %s", quote, username, year);

  // string functions

  return 0;
}