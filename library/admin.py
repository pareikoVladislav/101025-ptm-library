from django.contrib import admin

from library.models.authors import Author
from library.models.books import Book
from library.models.users import User, Membership
from library.models.library import Library
from library.models.publisher import Publisher
from library.models.category import Category
from library.models.posts import Posts
from library.models.borrow import Borrow
from library.models.events import Event, EventParticipant
from library.models.review import Review


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

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
        'gender',
        'age',
        'phone',
        'is_staff',
        'is_active',
        'date_joined',
    ]

    list_filter = [
        'role',
        'gender',
        'is_staff',
        'is_active',
        'date_joined',
    ]

    search_fields = [
        'username',
        'email',
        'first_name',
        'last_name',
        'phone',
    ]

    list_editable = [
        'role',
        'is_staff',
        'is_active',
    ]

    list_per_page = 50

@admin.register(Membership)
class MembershipModelAdmin(admin.ModelAdmin):
    list_display = [
        'member',
        'library',
        'joined_at',
    ]

    list_filter = [
        'library',
        'joined_at',
    ]

    search_fields = [
        'member',
        'library',
    ]

    list_editable = [
        'joined_at',
    ]

    list_per_page = 50

@admin.register(Library)
class LibraryModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'location',
        'website',
    ]

    list_filter = [
        'location',
    ]

    search_fields = [
        'name',
        'location',
        'website',
    ]

    list_editable = [
        'website',
    ]

    list_per_page = 50

@admin.register(Publisher)
class PublisherModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'country',
        'city',
        'address',
    ]

    list_filter = [
        'country',
        'city',
    ]

    search_fields = [
        'name',
        'country',
        'city',
        'address',
    ]

    list_editable = [
        'country',
        'city',
        'address',
    ]

    list_per_page = 50

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

    list_filter = [
        'name'
    ]

    search_fields = [
        'name'
    ]

    list_editable = [
        'name'
    ]

    list_per_page = 50

@admin.register(Posts)
class PostsModelAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'library',
        'moderated',
        'published_date',
        'updated_date',
    ]

    list_filter = [
        'moderated',
        'library',
        'author',
        'published_date',
        'updated_date',
    ]

    search_fields = [
        'title',
        'post_text',
        'author',
        'library',
    ]

    list_editable = [
        'moderated',
    ]

    list_per_page = 50

@admin.register(Borrow)
class BorrowModelAdmin(admin.ModelAdmin):
    list_display = [
        'member',
        'book',
        'library',
        'issue_date',
        'return_plane_date',
        'return_actual_date',
        'is_returned',
    ]

    list_filter = [
        'is_returned',
        'library',
        'issue_date',
        'return_plane_date',
    ]

    search_fields = [
        'member',
        'book',
        'library',
    ]

    list_editable = [
        'return_actual_date',
        'is_returned',
    ]

    list_per_page = 50

@admin.register(Event)
class EventModelAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'library',
        'date',
        'description',
    ]

    list_filter = [
        'library',
        'date',
        'books',
    ]

    search_fields = [
        'title',
        'description',
        'library',
        'books',
    ]

    list_editable = [
        'library',
        'date',
    ]

    list_per_page = 50

@admin.register(EventParticipant)
class EventParticipantModelAdmin(admin.ModelAdmin):
    list_display = [
        'event',
        'registration_date',
        'member',
    ]

    list_filter = [
        'event',
        'registration_date',
    ]

    search_fields = [
        'event',
        'member',
    ]

    list_editable = [
        'registration_date',
    ]

    list_per_page = 50

@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = [
        'book',
        'reviewer',
        'rating',
        'content',
    ]

    list_filter = [
        'rating',
        'book',
        'reviewer',
    ]

    search_fields = [
        'content',
        'book',
        'reviewer',
    ]

    list_editable = [
        'rating',
    ]

    list_per_page = 50
