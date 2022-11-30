# Exercise 15 - Payment Methods

class BankAccount:
    def __init__(self, name, balance, payment_method=None):
        self.__name = name
        self.__balance = balance
        self.__payment_method = payment_method

    def get_name(self):
        return self.__name

    def set_payment_method(self, payment_method):
        if issubclass(type(payment_method), PaymentMethod):
            self.__payment_method = payment_method

    def pay(self, amount):
        if self.__payment_method.pay(self.__balance, amount):
            self.__balance -= amount + self.__payment_method.get_service_fee()
            return True

        return False

    def get_service_fee(self):
        return self.__payment_method.get_service_fee()

    def get_balance(self):
        return self.__balance


class PaymentMethod:
    def __init__(self, service_fee=0):
        self.__service_fee = service_fee

    def get_service_fee(self):
        return self.__service_fee

    def pay(self, balance, amount):
        if balance >= amount:
            return True

        return False


class CreditCard(PaymentMethod):
    def __init__(self):
        super().__init__(10)


class E_Wallet(PaymentMethod):
    def __init__(self):
        super().__init__(5)


# Test Case

restaurant = {
    "burger": 10,
    "softdrink": 5,
    "pizza": 15
}

transaction_id = 0


def transaction(customer, items):
    global transaction_id
    transaction_id += 1
    print("*" * 30)
    print(f"Transaction ID: #{transaction_id:02d}")
    print(f"Customer: {customer.get_name()}")
    print(f"Starting Balance: ${customer.get_balance():.2f}")
    print("*" * 30)
    sum = 0
    for item in items:
        print(f"{item}: ${restaurant[item]:.2f}")
        sum += restaurant[item]
    print("*" * 30)
    print(f"Sub Total: ${sum:.2f}")
    print(f"Service fee: ${(customer.get_service_fee()):.2f}")
    print(f"Total: ${(sum + customer.get_service_fee()):.2f}")
    print("*" * 30)
    customer.pay(sum)
    print(f"Ending Balance: ${(customer.get_balance()):.2f}")
    print("*" * 30)
    print()


john = BankAccount("John", 100)
john.set_payment_method(CreditCard())
transaction(john, ["burger", "pizza", "softdrink"])

john = BankAccount("Jane", 100)
john.set_payment_method(E_Wallet())
transaction(john, ["pizza", "softdrink"])
