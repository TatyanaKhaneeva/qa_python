import pytest
from main import BooksCollector
class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2


    @ pytest.mark.parametrize('book', ['Идиот', 'Little women'])
    def test_add_new_book_positive(self, collector, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert collector.books_genre[book] == ''


    @pytest.mark.parametrize('book', ['', 'Жизнь, необыкновенные и удивительные приключения Робинзона Крузо'])
    def test_add_new_book_zero_or_too_many_symbols(self, book):
        collector = BooksCollector()
        assert not collector.add_new_book(book)

    def test_set_book_genre_valid_name(self, collector):
        collector.add_new_book('Собака Баскервиллей')
        collector.set_book_genre('Собака Баскервиллей', 'Детективы')
        assert collector.books_genre['Собака Баскервиллей'] == 'Детективы'


    @pytest.mark.parametrize('name, genre', [['Жизнь, необыкновенные и удивительные приключения Робинзона Крузо', 'Ужасы'], ['Путешествия в некоторые отдаленные страны света Лемюэля Гулливера, сначала хирурга, а потом капитана нескольких кораблей', 'Народная сказка']])
    def test_set_book_genre_long_name_not_valid_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert not collector.set_book_genre(name, genre)


    def test_get_book_genre_return_right_name(self, collector):
        collector.add_new_book('Хроники Нарнии')
        collector.set_book_genre('Хроники Нарнии', 'Фантастика')
        assert collector.get_book_genre('Хроники Нарнии') == 'Фантастика'

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Эй, Арнольд!')
        collector.set_book_genre('Эй, Арнольд!', 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Мультфильмы') \
               and type(collector.get_books_with_specific_genre('Мультфильмы')) == list


    def test_get_books_for_children_right_genre(self):
        collector = BooksCollector()
        books = ['Ронья, дочь разбойника', 'Приключения Муми Троллей', 'Белоснежка']
        list_of_books = 0
        for name in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, collector.genre[list_of_books])
            list_of_books += 1

        for rating in collector.genre_age_rating:
            assert rating not in collector.get_books_for_children()


    def test_get_books_for_children_with_adult_genre(self):
        collector = BooksCollector()
        books = ['Пятьдесят оттенков серого', 'Хлеб с ветчиной']
        book_list = 0
        for name in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, collector.genre_age_rating[book_list])
            book_list += 1

        assert not collector.get_books_for_children()


    def test_add_book_in_favorites(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        assert 'Война и мир' in collector.favorites


    def test_delete_book_from_favorites(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites('Война и мир')
        assert 'Война и мир' not in collector.favorites


    def test_get_list_of_favorites_books(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Harry Potter')
        collector.add_book_in_favorites('Harry Potter')
        assert collector.get_list_of_favorites_books() == ['Harry Potter']