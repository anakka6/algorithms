'''String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).'''


def string_compression(input_string):
    output_string = ''
    previous_character = None
    count = 1
    for char in input_string:
        if char == previous_character:
            count += 1
        elif previous_character is not None and char is not previous_character:
            output_string += previous_character + str(count)
            count = 1
        previous_character = char
    output_string += previous_character + str(count)
    if len(output_string) < len(input_string):
        return output_string
    else:
        return input_string


print(string_compression('aabcccccaaa'))
