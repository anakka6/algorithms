''' Write a Python program to calculate the harmonic sum of n-1. Go to the editor
Note: The harmonic sum is the sum of reciprocals of the positive integers.
Example :
harmonic series'''


def sum_harmonic_series(n):
    if n < 2:
        return 1
    else:
        #print(int(1 / n))
        return (1 / n) + sum_harmonic_series(n - 1)


print(sum_harmonic_series(7))
