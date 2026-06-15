from django.urls import path
from rest_framework.routers import DefaultRouter

from library.views.categories import CategoryListCreateGenericView
from library.views.books import BookListGenericView
from library.views.events import EventViewSet
from library.views.users import UserViewSet

router = DefaultRouter()
router.register('events', EventViewSet, basename='events')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('categories', CategoryListCreateGenericView.as_view()),
    path('books', BookListGenericView.as_view()),
    path('authors', CategoryListCreateGenericView.as_view()),
]

urlpatterns += router.urls
