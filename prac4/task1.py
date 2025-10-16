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

oruel = Book("Oruel", "1984", 1984)
print(oruel.info())
