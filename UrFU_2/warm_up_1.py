import re
def is_almost_lucky(ticket_number: str) -> bool:
    """
    Checks if the ticket number is "almost lucky".
    
    An "almost lucky" ticket is one where the sum of the first three digits
    differs from the sum of the last three digits by exactly 1 (in either direction).
    
    :param ticket_number: Six-digit ticket number
    :return: True if the ticket is "almost lucky", False otherwise
    """
    # TODO: Implement the check for an "almost lucky" ticket
    match = re.search(r'\d{6}', ticket_number)
    
    if not match:
        raise ValueError

    if ticket_number == '000000' or ticket_number == '999999':
        return False
    
    n_int = 0

    for i in range(len(ticket_number)):
        n_int += int(ticket_number[i]) * (10 ** (len(ticket_number) - i - 1))

    n_int_next = n_int + 1
    n_int_prev = n_int - 1
    
    sum_first_next = 0
    sum_second_next = 0
    sum_first_prev = 0
    sum_second_prev = 0

    for i in range(3):
        sum_first_next += n_int_next % 10
        n_int_next //= 10

        sum_first_prev += n_int_prev % 10
        n_int_prev //= 10

    for i in range(3):
        sum_second_next += n_int_next % 10
        n_int_next //= 10

        sum_second_prev += n_int_prev % 10
        n_int_prev //= 10

    return (sum_first_next == sum_second_next) or (sum_first_prev == sum_second_prev)