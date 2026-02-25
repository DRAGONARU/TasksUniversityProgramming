from typing import List


def compress_string(input_string: str) -> str:
    """
    Compress the input string by replacing consecutive repeating characters
    with the character followed by its count in parentheses.

    Args:
    input_string (str): The input string to compress.

    Returns:
    str: The compressed string.

    Example:
    >>> compress_string("aaabbbcccc")
    "a(3)b(3)c(4)"
    >>> compress_string("abcde")
    "abcde"
    """
    last_letter = ''
    ans = []
    ammount_of_repeating = 0
    for i in range(len(input_string)):
        current_letter = input_string[i]
        if current_letter != last_letter:
            ans.append(last_letter)
            if ammount_of_repeating > 1:
                ans.append('(' + str(ammount_of_repeating) + ')')
            ammount_of_repeating = 1
        else:
            ammount_of_repeating += 1
        last_letter = current_letter
    ans.append(last_letter)
    if ammount_of_repeating > 1:
        ans.append('(' + str(ammount_of_repeating) + ')')

    return ''.join(ans)


def decompress_string(compressed_string: str) -> str:
    """
    Decompress a string that was compressed using the compress_string function.

    Args:
    compressed_string (str): The compressed string to decompress.

    Returns:
    str: The decompressed (original) string.

    Example:
    >>> decompress_string("a(3)b(3)c(4)")
    "aaabbbcccc"
    >>> decompress_string("abcde")
    "abcde"
    """ 
    ans = []
    last_letter = ''
    i = 0
    while i < len(compressed_string):
        current_letter = compressed_string[i]
        if current_letter == '(':
            num = 0
            i += 1
            while compressed_string[i] != ')':
                num = num * 10 + int(compressed_string[i])
                i += 1
            ans.append(last_letter * num)
        elif (last_letter != '(') and (current_letter != ')')  and (current_letter != last_letter) and (last_letter != ')'):
            ans.append(last_letter)
        current_letter = compressed_string[i]
        last_letter = current_letter
        i += 1
    if last_letter != ')':
        ans.append(last_letter)

    return ''.join(ans)

print(decompress_string("a(3)b(3)c(4)"))
print(decompress_string("abcde"))