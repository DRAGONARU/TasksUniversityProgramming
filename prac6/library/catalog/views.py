from django.shortcuts import render

class book:
    '''
    Создаём класс книга
    У него есть атрибуты: название, автор, год
    '''
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book_1 = book('Мастер и Маргарита', 'Михаил Булгаков', '1966')

def books_detail(request):
    '''
    Функция для рендера страницы с информацией о книге
    '''
    book_info = {
        'name' : book_1.title,
        'author' : book_1.author,
        'year' : book_1.year
    }

    return render(request, 'catalog/books_detail.html', {'books_detail': book_info})