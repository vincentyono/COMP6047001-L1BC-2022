class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount: int) -> bool:
        if amount > 0:
            self.__balance += amount
            return True

        return False

    def pay(self, amount: int) -> bool:
        if self.__balance >= amount:
            self.__balance -= amount
            return True  # True if payment is successful

        return False  # False if payment is unsuccessful


class User:
    def __init__(self, username: str, balance: int):
        self.__username = username
        self.__bank_account = BankAccount(balance)  # BankAccount class

    def get_balance(self) -> int:
        return self.__bank_account.get_balance()

    def deposit(self, amount) -> bool:
        return self.__bank_account.deposit(amount)

    def pay(self, amount) -> bool:
        return self.__bank_account.pay(amount)


# Test Case


def transaction(item, user):
    return "Transaction Complete" if user.pay(item) else "Transaction Failed"


restaurant = {
    "burger": 10,
    "softdrink": 5
}

bookstore = {
    "comic": 10,
    "magazine": 7,
    "textbook": 50
}

john = User("John", 50)
print(transaction(restaurant["burger"], john))  # Output: Transaction Complete
print(transaction(restaurant["softdrink"], john))  # Output: Transaction Complete # nopep8
print(transaction(bookstore["comic"], john))  # Output: Transaction Complete
print(transaction(bookstore["textbook"], john))  # Output: Transaction Failed
john.deposit(50)
print(transaction(bookstore["textbook"], john))  # Output: Transaction Complete
