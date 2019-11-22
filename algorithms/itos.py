''' Write a Python program to converting an Integer to a string in any base.'''


def itos(m, base):
    if m == 0:
        return ''  # Use \n or space to denote EOF in python
    else:
        r = itos(int(m / base), base)
        return r + str(m % base)


def itos_iterative(input, base):
    output_string = ''
    while input != 0:
        stringDigit = str(input % base)
        input = int(input / base)
        output_string = stringDigit + output_string
    return output_string


# print(itos(25678797, 2))
# print(type(itos(25678797, 2)))
# print(type(str(256 % 10)))

# print(str(2) + str(3))

# print(itos_iterative(25678797, 2))
# print(type(itos_iterative(25678797, 2)))

print(itos(1, 10))
print(itos_iterative(0, 10))
