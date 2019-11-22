'''. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
'''


def sum_series(n, x):
    if n - x > 0:
        return n + sum_series(n - x, x)
    else:
        return n


print(sum_series(10, 2))


def sum_series_iterative(n, x):
    sum = 0
    while n >= 0:
        sum += n
        n = n - x
    return sum


print(sum_series_iterative(10, 2))


def sum_series_simpler(n):
    if n <= 0:
        return 0
    else:
        return n + sum_series_simpler(n - 2)


print(sum_series_simpler(10))
