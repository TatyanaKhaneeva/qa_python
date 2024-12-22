# qa_python
! Создание объекта вынесено фикстурой в файл conftest.py !
1. Тест проверяет добавление двух книг в список книг :
```
def test_add_new_book_add_two_books(self)
```
---
2. Тест с параметризацией проверяет добавление новых книг в список и что у вновь добавленных книг нет жанра :
```
@ pytest.mark.parametrize('book', ['Идиот', 'Little women'])
    def test_add_new_book_positive(self, collector, book):
```
---
3. Тест с параметризацией проверяет, что книги, в названии которых более 40 символов, не будут добавлены в список книг :
```
@pytest.mark.parametrize('book', ['', 'Жизнь, необыкновенные и удивительные приключения Робинзона Крузо'])
    def test_add_new_book_zero_or_too_many_symbols(self, book):
```
---
4. Тест проверяет добавление новых книг и присвоение этим книгам жанра :
```
 def test_set_book_genre_valid_name(self, collector):
```
---
5. Тест с параметризацией проверяет, что книга с названием 40+ символов и книга с невалидным названием жанра не добавляются в список :
```
@pytest.mark.parametrize('name, genre', [['Жизнь, необыкновенные и удивительные приключения Робинзона Крузо', 'Ужасы'], ['Путешествия в некоторые отдаленные страны света Лемюэля Гулливера, сначала хирурга, а потом капитана нескольких кораблей', 'Народная сказка']])
    def test_set_book_genre_long_name_not_valid_genre(self, name, genre):
```
---
6. Тест проверяет возвращение жанра книги по названию :
```
def test_get_book_genre_return_right_name(self, collector):
```
---
7. Тест проверяет выведение книг с по определенному жанру :
```
def test_get_books_with_specific_genre(self, collector):
```
---
8. Тест проверяет, что в списке соедржатся только детские книги :
```
def test_get_books_for_children_right_genre(self):
```
---
9. Тест проверяет, что в списке детских книг нет книг с жанром 18+ :
```
 def test_get_books_for_children_with_adult_genre(self):
```
---
10. Тест проверяет добавление книг в список "Favorites" :
```
def test_add_book_in_favorites(self, collector):
```
---
11. Тест проверяет удаление книг из списка "Favorites" :
```
def test_delete_book_from_favorites(self, collector):
```
---
12. Тест проверяет возвращение списка "Favorites" :
```
def test_get_list_of_favorites_books(self, collector):
```
---