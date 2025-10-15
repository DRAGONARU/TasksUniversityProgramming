import datetime
from decimal import Decimal

def add(items, title, amount, expiration_date=None):
    '''
    Функция для добавления товара
    :param items: словарь с товарами
    :param title: название товара
    :param amount: количество товара
    :param expiration_date: когда товар истекает
    '''
    if expiration_date is not None:
        expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
    if title in items:
        items[title].append({'amount': amount, 'expiration_date': expiration_date})
    else:
        items[title] = [
            {'amount': amount, 'expiration_date': expiration_date}
        ]

def add_by_note(items, note):
    '''
    Функция для добавления товара по строке
    :param items: словарь с товарами
    :param note: строка с описанием товара
    '''
    list_of_items = note.split()
    if '-' in list_of_items[-1]:
        title = ' '.join(list_of_items[:-2])
        amount = Decimal(list_of_items[-2])
        expiration_date = list_of_items[-1]
        add(items, title, amount, expiration_date)
    else:
        title = ' '.join(list_of_items[:-1])
        amount = Decimal(list_of_items[-1])
        add(items, title, amount)


def find(items, needle):
    '''
    Функция для поиска товара
    :param items: словарь с товарами
    :param needle: продукт
    '''
    needle = needle.lower()
    ans = []
    for item in items.keys():
        if needle in item.lower():
            ans.append(item)
    return ans


def amount(items, needle):
    '''
    Функция для подсчета количества товара
    :param items: словарь с товарами
    :param needle: продукт
    '''
    keys = find(items, needle)
    co = Decimal('0')

    for title, item in items.items():
        if title in keys:
            for am in item:
                co += am['amount']

    return co

DATE_FORMAT = '%Y-%m-%d'
goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}
