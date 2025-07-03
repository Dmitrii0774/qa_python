## Описание тестовых функций для класса *BooksCollector*

### Создание объекта вынесено фикстурой в conftest.py


1. Проверяет корректность добавления двух книг в коллекцию.
```
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2
```
---
2. Проверяет поведение коллектора при добавлении книги с названием,
        превышающим допустимый лимит символов.
```
    def test_add_long_book_name(self, collector):
        long_name = ("Aaaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa a")
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 0
```
---
3. Проверка защиты от добавления дубликатов
```
    def test_add_duplicate_book(self, collector):
        book_name = "Война миров" 
        collector.add_new_book(book_name) 
        initial_length = len(collector.books_genre)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == initial_length
```
---
4. Проверка корректности получения установленного жанра книги
```
    def test_get_book_genre_return_valid_name(self, collector):
        collector.add_new_book('Отроки во вселенной')
        collector.set_book_genre('Отроки во вселенной', 'Фантастика')
        assert len(collector.books_genre) == initial_length
```
---
5. Тест с параметризацией проверяет обработку недопустимых жанров
```
    @pytest.mark.parametrize(
        "invalid_genre",
        ["Роман", "Поэзия", "Драма", "Триллер", "Фэнтези"],
    )
    def test_set_book_genre_invalid_genre(self, collector, invalid_genre):
        collector.add_new_book("Тестовая книга")
        collector.set_book_genre("Тестовая книга", invalid_genre)
        assert collector.get_book_genre("Тестовая книга") == ""
```
---
6. Тест проверяет обработку случая, когда книги нет в коллекции
```
    def test_set_book_genre_non_existent_book(self, collector):
        collector.set_book_genre("Неизвестная книга", "Фантастика")
        assert "Неизвестная книга" not in collector.books_genre
```
---
7. Тест с параметризацией проверяет корректность работы метода 
    get_books_with_specific_genre в случае, когда запрашиваемый 
    жанр отсутствует в коллекции книг
```
    @pytest.mark.parametrize('name, genre',[['Том и Джерри', 'Мультфильмы'],['Отроки во вселенной', 'Фантастика']])
    def test_get_books_with_specific_genre_empty_list_book_false_genre(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert not collector.get_books_with_specific_genre('Антиутопия')
```
---
8. Тест проверяет корректность добавления книги в избранное при наличии
        книг в системе
```
    def test_add_book_in_favorites_when_books_in_list(self, collector):
        books = ['Книга_1', 'Книга_2', 'Книга_3', 'Книга_4']
        for name in books:
            collector.add_new_book(name)  # Добавляем каждую книгу в коллекцию
        collector.add_book_in_favorites('Книга_1')
        assert 'Книга_1' in collector.favorites
```
---
9. Тест проверяет корректности удаления книги из списка избранного
```
    def test_delete_book_from_favorites(self, collector):
        books = ['Книга_1', 'Книга_2', 'Книга_3']
        for name in books:
            collector.add_new_book(name)  
            collector.add_book_in_favorites(name)  
        collector.delete_book_from_favorites('Книга_1')
        assert 'Книга_1' not in collector.favorites
```
---
10. Тест проверяет поведение метода удаления книги из избранного,
        когда книга отсутствует в списке избранного
```
    def test_delete_book_from_favorites_no_name_in_list(self, collector):
        books = ['Книга_1', 'Книга_2', 'Книга_3']
        for name in books:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites('Книга_4')
        favorites_list = collector.get_list_of_favorites_books()
        assert len(favorites_list) == len(books)
        assert 'Книга_4' not in favorites_list
```
---
11. Тест проверяет корректность получения списка книг из избранного,
        когда список не пустой
```
    def test_get_list_of_favorites_books_not_empty(self, collector):
        books = ['Книга_1', 'Книга_2', 'Книга_3']
        for name in books:
            collector.add_new_book(name)  # Добавляем книгу в общую коллекцию
            collector.add_book_in_favorites(name)  # в избранное
        favorites_list = collector.get_list_of_favorites_books()
        assert len(favorites_list) == len(books)
        for book in books:
            assert book in favorites_list
```
---