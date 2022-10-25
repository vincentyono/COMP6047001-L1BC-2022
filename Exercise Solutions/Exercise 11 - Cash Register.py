def cash_register(price: int, cash: int) -> list:
    # List of all available bills
    bills = [100_000, 50_000, 20_000, 10_000,
             5_000, 2_000, 1_000, 500, 200, 100]

    change = []
    amount = cash - price

    i = 0  # it serve as index to iterate through bills list

    # loop runs when amount is larger than or equal to 100,
    # since our smallest bill is 100
    while amount >= 100:

        # if amount is larger than currently iterated bill
        if amount >= bills[i]:
            change.append(bills[i])  # add bill to change
            amount -= bills[i]  # decrease amount of change by the bill

        # if amount is smaller than currently iterated bill
        else:
            i += 1  # increment i by 1

    return change


# output: [20000, 5000] Rp.25,000
print(cash_register(75_000, 100_000),
      f"Rp.{sum(cash_register(75_000, 100_000)):,}")

print(
    cash_register(
        200200, 250_000), f"Rp.{sum(cash_register(200200, 250000)):,}"
)  # output: [20000, 20000, 5000, 2000, 2000, 500, 200, 100] Rp.49,800

# output: [50000, 500] Rp.50,500
print(cash_register(49500, 100_000),
      f"Rp.{sum(cash_register(49500, 100_000)):,}")

# output: [5000, 2000, 200] Rp.7,200
print(cash_register(12_700, 20_000),
      f"Rp.{sum(cash_register(12_700, 20_000)):,}")

# output: [10000, 1000] Rp.11,000
print(cash_register(9000, 20000), f"Rp.{sum(cash_register(9000, 20000)):,}")
