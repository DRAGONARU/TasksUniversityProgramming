from datetime import datetime

class Book:
    """Класс, представляющий книгу с названием, автором и годом издания."""

    def __init__(self, title: str, author: str, year: int):
        """
        Инициализирует экземпляр книги.

        Args:
            title (str): Название книги.
            author (str): Имя автора.
            year (int): Год издания книги.
        """
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
        """
        Возвращает строковое представление информации о книге.

        Returns:
            str: Форматированная строка с названием, автором и годом издания.
        """
        return f"{self.title} by {self.author} ({self.year})"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта при его печати или преобразовании в строку.

        Returns:
            str: Результат вызова метода `info()`.
        """
        return self.info()

    def __eq__(self, other: object) -> bool:
        """
        Сравнивает два объекта Book по названию.

        Args:
            other (object): Другой объект для сравнения.

        Returns:
            bool: True, если другой объект является экземпляром Book и имеет то же название, иначе False.
        """
        return isinstance(other, Book) and self.author == other.author

    @property
    def age(self) -> int:
        """
        Возвращает возраст книги в годах.

        Returns:
            int: Количество лет, прошедших с года издания книги до текущего года.
        """
        return datetime.now().year - self.year

    @age.setter
    def age(self, value: int) -> None:
        """
        Устанавливает год издания книги на основе заданного возраста.

        Args:
            value (int): Возраст книги в годах.
        """
        self.year = datetime.now().year - value

    @classmethod
    def from_string(cls, book_str: str) -> "Book":
        """
        Создаёт экземпляр Book из строки с данными.

        Args:
            book_str (str): Строка формата 'Название,Автор,Год'.

        Returns:
            Book: Новый экземпляр класса Book, созданный на основе переданных данных.
        """
        title, author, year = book_str.split(',')
        return cls(title.strip(), author.strip(), int(year))


class EBook(Book):
    """Класс, представляющий электронную книгу, наследуемую от Book."""

    def __init__(self, title: str, author: str, year: int, format: str):
        """
        Инициализирует экземпляр электронной книги.

        Args:
            title (str): Название книги.
            author (str): Имя автора.
            year (int): Год издания книги.
            format (str): Формат электронной книги (например, 'PDF', 'EPUB', 'MOBI').
        """
        super().__init__(title, author, year)
        self.format = format

    def info(self) -> str:
        """
        Возвращает строковое представление информации об электронной книге.

        Returns:
            str: Форматированная строка с названием, автором, годом издания и форматом.
        """
        return f"{super().info()} [{self.format}]"

oruel = Book("1984", "Oruel", 1984)

raskolnikov = EBook("Prestuplenie i nakazanie", "Fedor Dostoevsky", 1866, "pdf")
print(raskolnikov.info())
print(oruel.info())
print(raskolnikov)
print(oruel.age)
print(Book.from_string("abob, Dima, 2024").info())
print(Book.from_string("abob, Dima, 2024") == Book.from_string("ne abob, Dima, 2023"))
oruel.age = 20
print(oruel.age)
