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
