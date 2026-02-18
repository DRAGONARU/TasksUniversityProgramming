def custom_string_to_int(string_representation: str) -> int:
    """
    Converts a string representation of an integer to its corresponding int value.

    Args:
    string_representation (str): The string to convert. Must represent a valid integer.

    Returns:
    int: The integer value represented by the string.

    Raises:
    ValueError: If the input string is not a valid integer representation.
    """
    # TODO: Implement the conversion logic here
    if len(string_representation) == 0:
        raise ValueError
    
    is_minus = False
    start = 0

    if string_representation[0] == '-':
        start = 1
        is_minus = True
    
    nums_dict = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '0' : 0}
    
    result = 0

    for i in range(start, len(string_representation)):
        x_num = nums_dict.get(string_representation[i], -1)

        if x_num == -1:
            raise ValueError
        
        result *= 10
        result += x_num
    return result * -1 if is_minus else result

print(custom_string_to_int("123"))  # Вывод: 123
print(custom_string_to_int("-456"))  # Вывод: -456
print(custom_string_to_int("0"))  # Вывод: 0
print(custom_string_to_int("-0"))  # Вывод: 0

custom_string_to_int("12a3")  # Должно вызвать ValueError
'''
custom_string_to_int("")  # Должно вызвать ValueError
'''