import ast

def extract_list_from_assignment(s):
    '''
    Функция, что парсит лист из входных данных.
    Принимает на вход строку.
    Возвращает список.
    '''
    _, right = s.split('=', 1)
    result = ast.literal_eval(right.strip())
    return result

def roman_to_int(roman):
    '''
    Функция для перевода римского числа в арабское.
    Принимает на вход римское число.
    Возвращает арабское.
    '''
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(roman.upper()):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

def int_to_roman(num):
    '''
    Функция для перевода арабского числа в римское
    Принимает на вход арабское число.
    Возвращает римское.
    '''
    num = int(num)
    roman_pairs = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),(100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                   (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I') ]
    result = []
    for value, symbol in roman_pairs:
        while num >= value:
            result.append(symbol)
            num -= value
    return ''.join(result)

def starting_box():
    '''
    Основная функция для конвертации чисел.
    Возвращает массив в переведёнными числами.
    '''
    numbers_list = extract_list_from_assignment(input())
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ans = []
    if numbers_list[0][0] not in numbers:
        for i in numbers_list:
            ans.append(roman_to_int(i))
        return ans
    else:
        for i in numbers_list:
            ans.append(int_to_roman(i))
        return ans

print(starting_box())
