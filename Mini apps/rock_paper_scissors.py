import random  # Built-in python module, for more information: https://docs.python.org/3/library/random.html

# assign rock, paper scissors to variables
# it is unnecessary, but if there is a typo, it will be easier to spot
# since python will give an error if the variables is not defined
rock = "rock"
paper = "paper"
scissors = "scissors"

# prompt user for input
user = input("Please choose between [rock, paper, scissors]: ")

# assign random number to cpu ranging from 1 to 3
cpu = random.randint(1, 3)

# swap cpu value to rock, paper or scissors
if cpu == 1:
    cpu = rock  # if cpu is 1 turn it into rock
elif cpu == 2:
    cpu = paper  # if cpu is 2 turn it into paper
else:
    cpu = scissors  # else turn it into scissors

# print result

# if user chooses rock
if user == rock and cpu == rock:
    print(f"CPU chooses {cpu}")
    print("Tie")
elif user == rock and cpu == paper:
    print(f"CPU chooses {cpu}")
    print("You Lose")
elif user == rock and cpu == scissors:
    print(f"CPU chooses {cpu}")
    print("You win")

# if user chooses paper
elif user == paper and cpu == rock:
    print(f"CPU chooses {cpu}")
    print("You win")
elif user == paper and cpu == paper:
    print(f"CPU chooses {cpu}")
    print("Tie")
elif user == paper and cpu == scissors:
    print(f"CPU chooses {cpu}")
    print("You Lose")

# if user chooses rock
elif user == scissors and cpu == rock:
    print(f"CPU chooses {cpu}")
    print("You Lose")
elif user == scissors and cpu == paper:
    print(f"CPU chooses {cpu}")
    print("You win")
elif user == scissors and cpu == scissors:
    print(f"CPU chooses {cpu}")
    print("Tie")

# if user type other than rock, paper or scissors
else:
    print("Invalid input")
