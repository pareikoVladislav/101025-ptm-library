from django.contrib import admin

from library.models.authors import Author


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
