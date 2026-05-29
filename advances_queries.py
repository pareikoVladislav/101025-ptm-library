import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# ### **Задача 1: Общее количество книг и среднее кол-во страниц**
# **ТЗ:** Получить общее количество книг в базе данных и среднее кол-во страниц всех книг в одном запросе
from library.models import Book, Author, Borrow, User, Library
from django.db.models import Count, Avg, Min, Max, Sum, Q
from django.db.models.functions import Round

books = Book.objects.aggregate(count_books=Count('id'), avg_pages=Round(Avg('pages'), 2))

print(books)

### **Задача 2: Диапазон страниц**
# **ТЗ:** Найти минимальное кол-во, максимальное кол-во сраниц среди всех книг
min_max_pages = Book.objects.aggregate(min_pages=Min('pages'), max_pages=Max('pages'))

print(min_max_pages)

### **Задача 3: Количество книг по каждому жанру**
# **ТЗ:** Подсчитать количество книг в каждом жанре, отсортировать по убыванию количества
result = Book.objects.values("category").annotate(count_book=Count("id")).order_by("-count_book")

print(result)

### **Задача 4: Средняя цена книг по каждому издательству**
# **ТЗ:** Вычислить среднюю цену книг для каждого издательства и количество книг у каждого издательства
publishers = Book.objects.values("publisher").annotate(
    avg_price=Avg('price'),
    count_books=Count('pk')
)

print(publishers)

### **Задача 5: Авторы с количеством книг и средним рейтингом**
# **ТЗ:** Получить всех авторов с количеством написанных книг, отсортировать по убыванию количества книг
authors = Author.objects.values('id').annotate(count_books=Count("books"), avg_ratings=Avg('rating')).order_by(
    'count_books')

print(authors)

### **Задача 6: Топ-5 читателей по количеству активных займов**
# **ТЗ:** Найти 5 пользователей с наибольшим количеством невозвращенных книг (которые до сих пор не вернулись)
borrows = User.objects.values('username', 'role', 'age').annotate(
    borrows_count=Count('borrows', filter=Q(borrows__is_returned=False))
).order_by('-borrows_count')[:5]

print(borrows)

for value in borrows:
    print(f"'{value['username']}' {value['role']}, {value['age']} years - {value['borrows_count']}")

### **Задача 7: Библиотеки с общим количеством книг и средней ценой книг**
# **ТЗ:** Для каждой библиотеки вычислить общее количество всех книг и среднюю цену
books_in_library = Library.objects.values('name').annotate(count_books=Count('books'),
                                                           avg_price=Round(Avg('books__price'), 2))

print(books_in_library)

### **Задача 8: Книги с количеством займов и статусом популярности**
# **ТЗ:** Для каждой книги подсчитать количество займов и пометить как популярную (>3 займов) или обычную
