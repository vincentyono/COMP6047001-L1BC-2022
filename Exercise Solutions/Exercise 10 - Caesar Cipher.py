# Exercise 10 - Caesar Cipher

import string  # Built-in python module, for more information: https://docs.python.org/3/library/string.html


def decrypt_caesar_cipher(message: str, shift: int) -> str:
    alphabets = [*string.ascii_uppercase]
    decrypted_message = [*message]

    # loop through each character in the decrypted_message
    for i, character in enumerate(decrypted_message):
        isupper = character.isupper()  # check whether character is uppercase or not

        # if character is in alphabets use upper() because [*string.ascii_uppercase] is used
        if character.upper() in alphabets:

            #   decrypt each character
            decrypted_message[i] = alphabets[(
                alphabets.index(character) % len(alphabets)) - shift] if isupper else alphabets[(
                    alphabets.index(character.upper()) % len(alphabets)) - shift].lower()

    return "".join(decrypted_message)  # join the list into string


print(decrypt_caesar_cipher("Aopz pz h zljyla", 7))  # output: This is a secret
print(decrypt_caesar_cipher("Jupxarcqv jwm Yaxpajvvrwp", 9))  # output: Algorithm and Programming # nopep8
print(decrypt_caesar_cipher("Bzdrzq Bhogdq", 25))  # output: Caesar cipher
print(decrypt_caesar_cipher("Qrpelcgvat Pnrfne Pvcure", 13))  # output: Decrypting Caesar Cipher # nopep8
print(decrypt_caesar_cipher("Mjqqt Btwqi", 5))  # output: Hello World

# FYI: Please ignore nopep8 comment, it is a comment to tell my autoformatter to not format the line
