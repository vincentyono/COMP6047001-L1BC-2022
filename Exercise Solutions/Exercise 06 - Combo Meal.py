# Exercise 06 - Combo Meal

burger_selling_price = int(input("Enter burger selling price: "))
soda_selling_price = int(input("Enter soda selling price: "))
combo_meal_selling_price = int(input("Enter combo meal selling price: "))

# burger_selling_price = burger_cost + fixed_profit
# soda_selling_price = soda_cost + fixed_profit
# combo_meal_selling_price = burger_cost + soda_cost + fixed_profit

burger_cost = combo_meal_selling_price - soda_selling_price
soda_cost = combo_meal_selling_price - burger_selling_price
fixed_profit = combo_meal_selling_price - burger_cost - soda_cost

print(f"The fixed profit is ${fixed_profit:.2f}")
