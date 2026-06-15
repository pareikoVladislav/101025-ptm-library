"""Event: реализовать EventViewSet для управления событиями библиотеки.

Эндпоинты:
- GET/POST /api/v1/library/events/
- GET/PUT/PATCH/DELETE /api/v1/library/events/<id>/

Требования:
- Использовать ModelViewSet.
- В get_queryset реализовать фильтры через query params:
  - ?type=future – вернуть только будущие события (date >= сегодня).
  - ?type=past – только прошедшие (date < сегодня).
  - ?library=<name> – только события конкретной библиотеки.
- По умолчанию (без type) – все события."""
from rest_framework import viewsets
from django.utils import timezone

from library.serializers.event import EventsListSerializer, EventsDetailSerializer
from library.models.events import Event

class EventViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        events_total = Event.objects.all()
        event_type = self.request.query_params.get('type')
        if event_type:
            if event_type.lower() == 'future':
                events_total = events_total.filter(date__gt=timezone.now())
            elif event_type.lower() == 'past':
                events_total = events_total.filter(date__lte=timezone.now())
        library = self.request.query_params.get('library')
        if library:
            events_total = events_total.filter(library__name=library.lower())

        return events_total

    def get_serializer_class(self):
        if self.request.method == 'get':
            return EventsListSerializer
        return EventsDetailSerializer
