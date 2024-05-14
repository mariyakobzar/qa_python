import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('В')
        collector.add_new_book('123456789012345678901234567890123456789')
        assert len(list(collector.books_genre.keys())) == 3

    def test_add_new_book_add_second_book_false(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert len(list(collector.books_genre.keys())) == 1

    def test_add_new_book_false(self):
        collector = BooksCollector()
        collector.add_new_book('')
        collector.add_new_book('12345678901234567890123456789012345678901')
        assert len(list(collector.books_genre.keys())) == 0

    def test_set_book_genre_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Три поросенка')
        collector.set_book_genre('Три поросенка', 'Фантастика')
        assert collector.books_genre['Три поросенка'] == 'Фантастика'

    def test_get_book_genre_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Ужасы')
        assert collector.books_genre.get('Преступление и наказание') == 'Ужасы'

    def test_get_books_with_specific_genre_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Три поросенка')
        collector.add_new_book('Кот в сапогах')
        collector.add_new_book('Теремок')
        collector.set_book_genre('Три поросенка', 'Комедии')
        collector.set_book_genre('Кот в сапогах', 'Комедии')
        collector.set_book_genre('Теремок', 'Комедии')
        assert collector.get_books_with_specific_genre('Комедии') == ['Три поросенка', 'Кот в сапогах', 'Теремок']

    def test_get_books_with_specific_genre_negative_result(self):
        collector = BooksCollector()
        collector.add_new_book('Три поросенка')
        collector.add_new_book('Кот в сапогах')
        collector.add_new_book('Теремок')
        collector.set_book_genre('Три поросенка', 'Фантастика')
        collector.set_book_genre('Кот в сапогах', 'Комедии')
        collector.set_book_genre('Теремок', 'Комедии')
        assert collector.get_books_with_specific_genre('Комедии') == ['Кот в сапогах', 'Теремок']

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Три поросенка')
        collector.add_new_book('Кот в сапогах')
        collector.add_new_book('Теремок')
        collector.set_book_genre('Три поросенка', 'Фантастика')
        collector.set_book_genre('Кот в сапогах', 'Комедии')
        assert collector.books_genre == {'Три поросенка' : 'Фантастика', 'Кот в сапогах' : 'Комедии', 'Теремок' : ''}

    def test_get_books_for_children_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Алиса в стране чудес')
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Теремок')
        collector.set_book_genre('Алиса в стране чудес', 'Фантастика')
        collector.set_book_genre('Гарри Поттер', 'Комедии')
        collector.set_book_genre('Теремок', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Алиса в стране чудес', 'Гарри Поттер', 'Теремок']

    def test_get_books_for_children_negative_result(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Кот в сапогах')
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Властелин колец', 'Ужасы')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Детективы')
        assert collector.get_books_for_children() == []

    def test_delete_book_from_favorites_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Сказки')
        collector.add_book_in_favorites('Сказки')
        collector.delete_book_from_favorites('Сказки')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        collector.add_new_book('Сказки')
        collector.add_new_book('Басни')
        collector.add_new_book('Стихи')
        collector.add_book_in_favorites('Сказки')
        collector.add_book_in_favorites('Басни')
        collector.add_book_in_favorites('Стихи')
        assert collector.favorites == ['Сказки', 'Басни', 'Стихи']

@pytest.mark.parametrize('name', ['Война и мир', 'В', '123456789012345678901234567890123456789'])
def test_add_new_book_false(name):
    collector = BooksCollector()
    collector.add_new_book(name)
    assert len(list(collector.books_genre.keys())) == 1
@pytest.mark.parametrize('name', ['Война и мир', 'Три товарища', 'Анна Каренина'])
def test_add_book_in_favorites_true(name):
    collector = BooksCollector()
    collector.add_new_book(name)
    collector.add_book_in_favorites(name)
    assert collector.favorites == [name]
@pytest.mark.parametrize('name', ['Война и мир', 'Три товарища', 'Анна Каренина'])
def test_add_book_in_favorites_false(name):
    collector = BooksCollector()
    collector.add_book_in_favorites(name)
    assert collector.favorites == []
