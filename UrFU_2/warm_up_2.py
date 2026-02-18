def rational_to_decimal(numerator: int, denominator: int, precision: int = 10) -> str:
    """
    Converts a rational number to its decimal representation.

    Args:
    numerator (int): The numerator of the rational number.
    denominator (int): The denominator of the rational number.
    precision (int, optional): The number of decimal places. Defaults to 10.

    Returns:
    str: The decimal representation of the rational number.

    Raises:
    ValueError: If the denominator is zero.
    """
    # TODO: Implement the conversion logic here
    if denominator == 0:
        raise ValueError
    if (type(denominator) is not int) or (type(numerator) is not int) or (type(precision) is not int):
        raise ValueError
    
    sign = '-' if (numerator * denominator) < 0 else ''
    numerator, denominator = abs(numerator), abs(denominator)

    integer_part = numerator // denominator
    remainder = numerator % denominator

    result = [f"{sign}{integer_part}."]
    remainder_positions = {}
    first_remainder = remainder

    position = 0
    while remainder != 0 and position < precision:
        if remainder in remainder_positions:
            start = remainder_positions[remainder]
            result.insert(start + 1, "(")
            result.append(")")
            return ''.join(result)

        remainder_positions[remainder] = position

        remainder *= 10
        digit = remainder // denominator
        result.append(str(digit))
        remainder %= denominator

        position += 1
    
    if remainder == 0 and result[-1][-1] == ".":
        result.append("0")

    if remainder != 0 and remainder == first_remainder:
        result.insert(1, "(")
        result.append(")...")
        return ''.join(result)
    
    if remainder != 0:
        result.append("...")
     
    return ''.join(result)

print(rational_to_decimal(1, 2))  # Вывод: "0.5"
print(rational_to_decimal(1, 3))  # Вывод: "0.(3)"
print(rational_to_decimal(5, 6))  # Вывод: "0.8(3)"
print(rational_to_decimal(-1, 4))  # Вывод: "-0.25"
print(rational_to_decimal(1, 7, 6))  # Вывод: "0.
print(rational_to_decimal(1234567, 9876543))  # Вывод: "0.67"
print(rational_to_decimal(0, 5))  # Вывод: "0"
