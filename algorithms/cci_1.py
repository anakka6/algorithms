'''Check if a string has unique characters'''

A = 'evening'


B = {}.fromkeys(A, 0)


def isUnique(input_string):
    dict_string = {}.fromkeys(input_string, 0)
    if len(input_string) is not len(dict_string):
        print(f'The string {input_string} does not have unique characters')
    else:
        print(f'The string {input_string} has unique characters')
    return


isUnique('Python')
