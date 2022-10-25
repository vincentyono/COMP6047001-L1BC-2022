# Exercise 01 - Split bill calculator

amount_of_bill = int(input("Enter amount of bill: "))
number_of_people = int(input("Enter number of people: "))
tips_percentage = int(input("Enter amount of tips (%): "))

total_tips = amount_of_bill * (tips_percentage / 100)
total_per_person = (amount_of_bill + total_tips) / number_of_people
tip_per_person = total_tips / number_of_people

print()  # Spacing between input and output

print(f"Tip Amount per person ${tip_per_person:.2f}")
print(f"Total Amount per person ${total_per_person:.2f}")
