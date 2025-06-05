import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.fixture
    def collector(self):
        return BooksCollector()


    # Тесты для add_new_book
    def test_add_new_book_success(collector):
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.books_genre


    def test_add_new_book_empty_genre(collector):
        collector.add_new_book("Война и мир")
        assert collector.books_genre["Война и мир"] == ""


    def test_add_existing_book(collector):
        collector.add_new_book("Война и мир")
        collector.add_new_book("Война и мир")
        assert len(collector.books_genre) == 1


    def test_add_long_book_name(collector):
        long_name = "A" * 41
        assert not collector.add_new_book(long_name)


    # Тесты для set_book_genre
    def test_set_genre_success(collector):
        collector.add_new_book("Американские боги")
        collector.set_book_genre("Американские боги", "Фантастика")
        assert collector.books_genre["Американские боги"] == "Фантастика"


    def test_set_invalid_genre(collector):
        collector.add_new_book("Американские боги")
        collector.set_book_genre("Американские боги", "Ужастики")
        assert collector.books_genre["Американские боги"] == ""


    # Тесты для get_book_genre
    def test_get_book_genre_success(collector):
        collector.add_new_book("Лунный камень")
        collector.set_book_genre("Лунный камень", "Детективы")
        assert collector.get_book_genre("Лунный камень") == "Детективы"


    def test_get_book_genre_non_existent_book(collector):
        assert collector.get_book_genre("Какая-то книга") is None


    # Тесты для get_books_with_specific_genre
    def test_get_books_by_genre(collector):
        collector.add_new_book("Чебурашка")
        collector.set_book_genre("Чебурашка", "Мультфильмы")
        collector.add_new_book("Бойцовский клуб")
        collector.set_book_genre("Бойцовский клуб", "Фантастика")
        collector.add_new_book("Американские боги")
        collector.set_book_genre("Американские боги", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Бойцовский клуб", "Американские боги"]


    # Тесты для get_books_for_children
    def test_get_children_books(collector):
        collector.add_new_book("Лунтик")
        collector.set_book_genre("Лунтик", "Мультфильмы")
        collector.add_new_book("Фиксики")
        collector.set_book_genre("Фиксики", "Фантастика")
        assert collector.get_books_for_children() == ["Лунтик", "Фиксики"]


    # Тесты для add_book_in_favorites
    def test_add_to_favorites(collector):
        collector.add_new_book("Букварь")
        collector.add_book_in_favorites("Букварь")
        assert "Букварь" in collector.favorites


    def test_add_duplicate_to_favorites(collector):
        collector.add_new_book("Букварь")
        collector.add_book_in_favorites("Букварь")
        collector.add_book_in_favorites("Букварь")
        assert len(collector.favorites) == 1


    # Тесты для delete_book_from_favorites
    def test_delete_from_favorites(collector):
        collector.add_new_book("Букварь")
        collector.add_book_in_favorites("Букварь")
        collector.delete_book_from_favorites("Букварь")
        assert "Букварь" not in collector.favorites


    # Тесты для get_list_of_favorites_books
    def test_get_favorites_list(collector):
        collector.add_new_book("Букварь")
        collector.add_new_book("Метро")
        collector.add_book_in_favorites("Букварь")
        collector.add_book_in_favorites("Метро")
        assert collector.get_list_of_favorites_books() == ["Букварь", "Метро"]