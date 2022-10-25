# Exercise 07 - Pig Latin

# NOTE: If you are confuse try to use the debugging feature in your pycharm or you can also use python tutor https://pythontutor.com/

vowels = ["a", "e", "i", "o", "u"]

# Turn input into a lists with space as separator
english = input("Please enter english sentence: ").split(" ")

# use enumerate function so we can access the index
for i, word in enumerate(english):
    # check whether word is title case
    istitle = word.istitle()

    # if the first letter of the word is vowel
    if word[0].lower() in vowels:
        english[i] = word + "yay"

    # if the first letter of the word is consonant
    else:
        # loop through each character of the word
        # use enumerate function so we can access the index
        for j, character in enumerate(word):

            # if the character is vowel or is the last character of the word
            if character in vowels or j == len(word) - 1:
                # record the index
                temp = j
                # break the loop
                break

        # if the word is in title case
        # word[temp:] all the characters from the first vowel
        # word[0:temp] from the first character to the character before the first vowel
        english[i] = (word[temp:].title() if istitle else word[temp:]
                      ) + word[0:temp].lower() + "ay"

# join the lists and turn it into string
pig_latin = " ".join(english)

# print results
print(f"Pig Latin: {pig_latin}")
