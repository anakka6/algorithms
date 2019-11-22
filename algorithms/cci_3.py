''' Replace spaces in a string with %20'''


def replace_string(input_string):
    t = ''
    for char in input_string:
        if char == ' ':
            char = '%20'
        t += char
    return t


print(replace_string('abh ina'))
