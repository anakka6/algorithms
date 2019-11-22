'''Given two strings, write a method to decide if one is a permutation of the other'''

def create_dictionaries(string):
    dict = {}
    for char in string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 0
    return dict

def isPermutation(input_string1, input_string2):
    dict1 = create_dictionaries(input_string1)
    dict2 = create_dictionaries(input_string2)
    if dict1 == dict2:
        print(f'{input_string2} is a permutation of {input_string1}')
    else:
        print(f'{input_string2} is not a permutation of {input_string1}')
    return None

isPermutation('pythonlearn','pthonynearl')

# How can this be solved in O(nlogn)? - By sorting

# could have created arrays instead of hash tables. But wait, the order of complexity is same in both cases.
