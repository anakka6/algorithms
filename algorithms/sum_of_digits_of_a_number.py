'''Write a Python program to get the sum of a non-negative integer.
Test Data:
sumDigits(345) -> 12
sumDigits(45) -> 9 '''


def sumDigits(n):
    if int(n / 10) == 0:
        return n
    else:
        return n % 10 + sumDigits(int(n / 10))


print(sumDigits(345))


def sumDigits_iterative(n):
    sum = 0
    while (n != 0):
        sum += n % 10
        n = int(n / 10)
    sum += n
    return sum


print(sumDigits_iterative(345))
