from django.contrib import admin

from library.models.authors import Author
from library.models.books import Book


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'surname',
        'date_for_birth',
        'rating',
        'deleted',
    ]

    list_filter = [
        'deleted',
        'rating'
    ]

    search_fields = [
        'name',
        'surname',
        'profile',
    ]

    list_editable = [
        'rating',
        'deleted',
    ]

    list_per_page = 50

@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'author',
        'published_date',
        'category',
        'publisher',
        'owner',
        'price',
        'discounted_price',
        'pages',
    ]

    list_filter = [
        'published_date',
        'category',
        'author',
        'publisher',
        'libraries',
    ]

    search_fields = [
        'name',
        'description',
        'author',
        'publisher',
        'category',
    ]

    list_editable = [
        'category',
        'publisher',
        'price',
        'discounted_price',
    ]

    list_per_page = 50
