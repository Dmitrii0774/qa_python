# Импортируем библиотеку pytest для написания тестов
import pytest

# Импортируем класс BooksCollector из файла main.py
from main import BooksCollector


# Определяем фикстуру с именем books_collector
@pytest.fixture(scope='function')
def collector():
    """
    Создает и возвращает новый экземпляр класса BooksCollector
    для тестирования операций с книгами.

    Возвращаемое значение:
    BooksCollector - новый экземпляр коллекции книг
    """
    collector = BooksCollector()

    return collector
