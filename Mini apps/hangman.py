import random  # Built-in python module, for more information: https://docs.python.org/3/library/random.html
import string  # Built-in python module, for more information: https://docs.python.org/3/library/string.html


# List of words that will be used in the game as answer (words with no spaces otherwise need more input checking)
word_bank = ["Apple", "Ball", "Cat", "Dog", "Elephant", "FLower", "House", "Igloo", "Jellyfish", "King", "Lion", "Moon",
             "Nurse", "Orange", "Panda", "Queen", "Rabbit", "Sun", "Tree", "Umbrella", "Violet", "Walrus", "Xylophone", "Zebra"]

# List of characters taken randomly from word_bank
# random.choice() picks a random word from word_bank
# lower() to turn answer into lowercase alternatively upper() can also be used
# * to split the word into characters
# Example: ['a', 'p', 'p', 'l', 'e'] or ['k', 'i', 'n', 'g']
#
# Other way to do it is:
# answer = []
# for alphabet in random.choice(word_bank):
#     answer.append(alphabet.lower())

answer = [*random.choice(word_bank).lower()]

# List of all attempted characters by the player
attempts = []

# List of "_" with the same length as answer
#
# Other way to do it is:
# word = []
# for i in answer:
#     word.append("_")

word = ["_" for i in answer]

# Lives of the player
lives = 5

# The loops runs when '_' is in word
# and lives > 0
# meaning the loops runs when the player hasn't guessed all the characters and
# lives is greater than 0
while ("_" in word) and (lives > 0):

    # print lives
    print(f"lives: {lives}")

    # print list of attempted characters
    # use join to make it from list to a string
    # Format of join function: string.join(list)
    # Example:
    #   s = '-'
    #   word = ['python', 'is', 'awesome']
    #   s.join(word) # output: python-is-awesome
    print(f"attempts: {' '.join(attempts)}")
    print(f"word: {' '.join(word)}")

    # prompt player to enter a character and turn it into lowercase for case-insensitive alternatively upper() can also be used
    player = input("Please enter a character: ").lower()

    # if player enters 1 character (len(player) == 1) and
    # player enters alphabet (player in [*string.ascii_lowercase]) if upper() is used change this into [*string.ascii_uppercase]
    # player haven't guessed the character (player not in attempts)
    if (len(player) == 1) and (player in [*string.ascii_lowercase]) and (player not in attempts):

        # append input from player into attempts
        attempts.append(player)

        # update word so if player guessed the character correctly it will shown as character rather than '_'
        #
        # Other way of doing this:
        #
        # word = []  # word into an empty list
        # for characters in answer:
        #     if characters in attempts:
        #         word.append(characters)
        #     else:
        #         word.append('_')

        word = [i if i in attempts else "_" for i in answer]

        # if player guessed the character wrongly
        if player not in answer:
            # lives decrease by 1
            lives -= 1

    # if player already guessed the character
    elif (player in attempts):
        print("You've attempted it already")

    else:
        print("Invalid input")

# if player guessed the character all the word
if ("_" not in word):
    print(f"The word is {''.join(word)}")
    print("You wins")
else:
    print(f"The word is {''.join(answer)}")
    print("You lose")
