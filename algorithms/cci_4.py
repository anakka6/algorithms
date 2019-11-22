'''Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
1.5
1.6
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)'''


def permutation_palindrome(input_string):
    string_dict = {}
    for char in input_string:
        if char in string_dict:
            string_dict[char] *= -1
        else:
            string_dict[char] = -1
    count = 0
    for element in string_dict:
        if string_dict[element] == -1:
            count += 1
    if count > 1:
        print('Not a palindrome permuation string')
    else:
        print('Yes! A palindrome permutation string')
    return None


permutation_palindrome('cactt')
