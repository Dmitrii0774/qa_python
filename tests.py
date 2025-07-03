import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше
# приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        """
        Тест проверяет корректность добавления двух книг в коллекцию.

        Проверяемые сценарии:
        - Добавление первой книги в пустую коллекцию
        - Добавление второй книги
        - Проверка общего количества книг

        Ожидаемый результат:
        После добавления двух книг коллекция должна содержать оба экземпляра
        с корректным количеством записей.
        """
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод books_genre,
        # имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный
    # экземпляр класса BooksCollector()

    def test_add_long_book_name(self, collector):
        """
        Тест проверяет поведение коллектора при добавлении книги с названием,
        превышающим допустимый лимит символов.

        Ожидаемое поведение: книга не должна быть добавлена в коллекцию,
        так как её название слишком длинное.
        """
        # Создаём название книги, превышающее допустимый лимит символов
        long_name = ("Aaaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa a")

        # Пытаемся добавить книгу в коллекцию (41 символ)
        collector.add_new_book(long_name)

        # Проверяем, что книга не была добавлена в коллекцию
        assert len(collector.get_books_genre()) == 0

    def test_add_duplicate_book(self, collector):
        """
        Тест проверки защиты от добавления дубликатов
        """
        book_name = "Война миров"  # Выбираем название книги
        collector.add_new_book(book_name)  # Первое добавление

        # Сохраняем начальную длину коллекции
        initial_length = len(collector.books_genre)

        # Пытаемся добавить ту же книгу повторно
        collector.add_new_book(book_name)

        # Проверяем, что длина не изменилась
        assert len(collector.get_books_genre()) == initial_length

    def test_get_book_genre_return_valid_name(self, collector):
        """
        Тест проверяет корректность получения установленного жанра книги.

        Сценарий тестирования:
        1. Добавление новой книги в коллекцию
        2. Установка жанра для книги
        3. Проверка корректности получения установленного жанра

        Ожидаемый результат: метод get_book_genre должен вернуть
        установленный жанр 'Фантастика'
        """
        # Добавление новой книги в коллекцию
        collector.add_new_book('Отроки во вселенной')

        # Установка жанра для книги
        collector.set_book_genre('Отроки во вселенной', 'Фантастика')

        # Проверяем, что установленный жанр соответствует ожидаемому результату
        assert collector.get_book_genre('Отроки во вселенной') == 'Фантастика'

    @pytest.mark.parametrize(
        "invalid_genre",
        ["Роман", "Поэзия", "Драма", "Триллер", "Фэнтези"],
    )
    def test_set_book_genre_invalid_genre(
        self, collector, invalid_genre
    ):
        """
        Тест проверяет обработку недопустимых жанров
        """
        collector.add_new_book("Тестовая книга")

        # Проверяем, что при установке недопустимого жанра ничего не меняется
        collector.set_book_genre("Тестовая книга", invalid_genre)
        assert collector.get_book_genre("Тестовая книга") == ""

    def test_set_book_genre_non_existent_book(self, collector):
        """
        Тест проверяет обработку случая, когда книги нет в коллекции
        """
        # Пытаемся установить жанр для несуществующей книги
        collector.set_book_genre("Неизвестная книга", "Фантастика")
        assert "Неизвестная книга" not in collector.books_genre

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Том и Джерри', 'Мультфильмы'],
            ['Отроки во вселенной', 'Фантастика']
        ]
    )
    def test_get_books_with_specific_genre_empty_list_book_false_genre(
        self, collector, name, genre
    ):
        """
        Тест проверяет корректность работы метода get_books_with_specific_genre
        в случае, когда запрашиваемый жанр отсутствует в коллекции книг.

        Ожидаемый результат:
        Метод должен возвращать пустой список, так как запрашиваемый жанр
        'Антиутопия' отсутствует в коллекции книг
        """
        # Добавляем новую книгу в коллекцию
        collector.add_new_book(name)

        # Устанавливаем жанр для книги
        collector.set_book_genre(name, genre)

        # Проверяем, что поиск книг по несуществующему жанру возвращает пустой
        # список
        assert not collector.get_books_with_specific_genre('Антиутопия')

    def test_add_book_in_favorites_when_books_in_list(self, collector):
        """
        Тест проверяет корректность добавления книги в избранное при наличии
        книг в системе
        """
        # Создаем список тестовых книг
        books = ['Книга_1', 'Книга_2', 'Книга_3', 'Книга_4']

        # Добавляем все книги в систему
        for name in books:
            collector.add_new_book(name)  # Добавляем каждую книгу в коллекцию

        # Пытаемся добавить конкретную книгу в избранное
        collector.add_book_in_favorites('Книга_1')

        # Проверяем, что книга успешно добавилась в список избранного
        assert 'Книга_1' in collector.favorites

    def test_delete_book_from_favorites(self, collector):
        """
        Тест проверки корректности удаления книги из списка избранного.

        Проверяет:
        - добавление книг в общую коллекцию
        - добавление книг в избранное
        - корректное удаление книги из избранного
        - проверку отсутствия удаленной книги в списке избранного
        """
        # Создаем список тестовых книг
        books = ['Книга_1', 'Книга_2', 'Книга_3']

        # Добавляем каждую книгу в коллекцию и в избранное
        for name in books:
            collector.add_new_book(name)  # Добавляем книгу в общую коллекцию
            collector.add_book_in_favorites(name)  # в избранное

        # Удаляем конкретную книгу из избранного
        collector.delete_book_from_favorites('Книга_1')

        # Проверяем, что удаленная книга отсутствует в списке избранного
        assert 'Книга_1' not in collector.favorites

    def test_delete_book_from_favorites_no_name_in_list(self, collector):
        """
        Тест проверяет поведение метода удаления книги из избранного,
        когда книга отсутствует в списке избранного.

        Сценарий теста:
        1. Создается список из трех книг
        2. Все книги добавляются в избранное
        3. Попытка удалить несуществующую книгу
        4. Ожидаемый результат: метод возвращает False

        """
        books = ['Книга_1', 'Книга_2', 'Книга_3']
        for name in books:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)
        # Пробуем удалить несуществующую книгу
        collector.delete_book_from_favorites('Книга_4')
        # Проверяем, что список не изменился
        favorites_list = collector.get_list_of_favorites_books()
        assert len(favorites_list) == len(books)
        # Проверяем отсутствие удаляемой книги в списке
        assert 'Книга_4' not in favorites_list

    def test_get_list_of_favorites_books_not_empty(self, collector):
        """
        Тест проверяет корректность получения списка книг из избранного,
        когда список не пустой.

        Ожидаемый результат:
        Метод должен вернуть непустой список книг из избранного
        """
        # Создаем список тестовых книг
        books = ['Книга_1', 'Книга_2', 'Книга_3']

        # Добавляем каждую книгу в общую коллекцию и в избранное
        for name in books:
            collector.add_new_book(name)  # Добавляем книгу в общую коллекцию
            collector.add_book_in_favorites(name)  # в избранное
        # Получаем список избранных книг
        favorites_list = collector.get_list_of_favorites_books()
        # Проверяем, что список не пустой
        assert len(favorites_list) == len(books)

        # Проверяем содержимое списка
        for book in books:
            assert book in favorites_list

    def test_set_book_genre(self, collector):
        """
        Тест проверки корректной установки жанра книги
        """
        book_name = 'Марсианин'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        # Проверяем установку жанра
        assert collector.get_books_genre()[book_name] == genre

    def test_get_books_with_specific_genre(self, collector):
        """
        Тест проверки получения книг определенного жанра
        """
        books = {
            'Марсианин': 'Фантастика',
            'Оно': 'Ужасы',
            'Шерлок Холмс': 'Детективы',
            'Том и Джерри': 'Мультфильмы',
            'Один дома': 'Комедии'
        }

        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        # Проверяем получение всех книг жанра Фантастика
        assert collector.get_books_with_specific_genre('Фантастика') == ['Марсианин']

    def test_get_books_genre(self, collector):
        """
        Тест проверки корректности получения словаря жанров
        """
        books = {
            'Интерстеллар': 'Фантастика',
            'Сияние': 'Ужасы',
            'Код да Винчи': 'Детективы',
            'Ну, погоди!': 'Мультфильмы',
            'Американский пирог': 'Комедии'
        }

        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        # Проверяем весь словарь жанров
        assert collector.get_books_genre() == books

    def test_get_books_for_children(self, collector):
        """
        Тест проверки получения книг для детей
        """
        books = {
            'Ну, погоди!': 'Мультфильмы',  # Детская
            'Марсианин': 'Фантастика',     # Детская
            'Том и Джерри': 'Мультфильмы',  # Детская
            'Оно': 'Ужасы',                # Не детская
            'Малыш и Карлсон': 'Мультфильмы',  # Детская
            'Гарри Поттер': 'Фантастика',  # Детская
            'Шерлок Холмс': 'Детективы'   # Не детская
        }

        # Добавляем все книги в коллектор
        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        # Формируем ожидаемый результат - без жанров Ужасы и Детективы
        expected_children_books = [
            'Ну, погоди!',
            'Марсианин',
            'Том и Джерри',
            'Малыш и Карлсон',
            'Гарри Поттер'
        ]

        # Проверяем результат
        result = collector.get_books_for_children()
        assert sorted(result) == sorted(expected_children_books)
