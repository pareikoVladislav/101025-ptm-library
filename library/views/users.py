"""User: сделать UserViewSet, который умеет отдавать "обогащённое" представление пользователя.

Эндпоинты:
- GET/POST /api/v1/users/
- GET/PUT/PATCH/DELETE /api/v1/users/<id>/

Требования:
- Использовать ModelViewSet.
- В get_serializer_context:
  - Прочитать query param ?include_related=true/false.
  - Положить флаг include_related в context сериализатора.
- В сериализаторе для list:
  - Переопределить to_representation(instance), чтобы:
    - Всегда отдавать базовые поля (id, username, email, role, age).
    - Если include_related=True:
      - добавить список библиотек пользователя (id, name);
      - добавить количество постов и отзывов;
      - добавить топ-3 отзыва пользователя по рейтингу (id, book_id, rating).
- В get_queryset/list предусмотреть prefetch_related/select_related, чтобы избежать N+1 при include_related=True."""
from django.db.models import Prefetch
from rest_framework import viewsets

from library.models import Membership
from library.serializers.user import UserListSerializer
from library.models.users import User

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.prefetch_related(
        'reviews', 'posts',
        Prefetch(
            'membership_records', queryset=Membership.objects.select_related('library')
    )
    )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        include_related = self.request.query_params.get('include_related', 'false')
        context['include_related'] = include_related.lower().strip() == 'true'
        return context
