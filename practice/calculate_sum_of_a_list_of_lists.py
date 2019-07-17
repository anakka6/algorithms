'''. Write a Python program of recursion list sum. Go to the editor
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21
'''


def sum_of_a_list(inputList):
    if len(inputList) == 0:
        return 0
    elif len(inputList) == 1 and type(inputList[0]) == int:
        return inputList[0]
    else:
        if type(inputList[0]) == list:
            list_value = sum_of_a_list(inputList[0])
        else:
            list_value = inputList[0]
        return list_value + sum_of_a_list(inputList[1:])


A = [1, 2, [3, 4], [5, 6]]

print(sum_of_a_list(A))
