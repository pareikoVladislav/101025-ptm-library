from rest_framework import serializers

from library.models.events import Event

class EventsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        field = ['id', 'title', 'date', 'library']


class EventsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'