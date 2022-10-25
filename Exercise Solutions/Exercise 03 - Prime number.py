# Exercise 03 - Prime number


def isprime(n: int) -> bool:
    # check if it is divisible to every number from 2 to (n - 1)
    for i in range(2, n):
        if n % i == 0:
            return False

    return n > 1


print(isprime(1))
print(isprime(25))  # output: False
print(isprime(13))  # output: True
print(isprime(8011))  # output: True
print(isprime(7517))  # output: True
print(isprime(12083))  # output: False
