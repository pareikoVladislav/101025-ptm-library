from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    library = models.ForeignKey(
        'Library',
        on_delete=models.CASCADE,
        related_name='events'
    )
    books = models.ManyToManyField(
        'Book',
        related_name='events'
    )

    def __str__(self):
        return f"Событие {self.title} от {self.date}"


class EventParticipant(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='participants'
    )
    member = models.ManyToManyField(
        'User',
        related_name='events'
    )
    registration_date = models.DateTimeField(default=timezone.now)

    def get_participant_count(self):
        return self.member.count()

    get_participant_count.short_description = 'count_participants'

    def __str__(self):
        users = [user.username for user in self.member.all()]
        return f"Event {self.event.title} Participants: {users} in {self.registration_date}"
        users_cnt = self.member.count()
        return f"Event {self.event.title} subscribed {users_cnt} people"
