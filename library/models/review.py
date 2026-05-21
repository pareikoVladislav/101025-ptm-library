from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Review(models.Model):
    content = models.TextField()
    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    reviewer = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.FloatField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
        null=True,
        blank=True
    )

    def __str__(self):
        rating = self.rating if self.rating else 'NA'
        return f"Review on the book: {self.book.name} by {self.reviewer.username} with rate: {rating}"
