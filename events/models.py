from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class Event(models.Model):
    """
    Represents an event entity.

    Attributes:
        title (str): The title of the event.
        description (str): The description of the event.
        date (Date): The date of the event.
        time (Time): The time of the event.
        location (str): The location of the event.
        status (int): The status of the event (0 for Draft, 1 for Published).
        created_on (DateTime): The date and time when the event was created.
        author (User): The user who created the event :model:`auth.User`.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="event_created_by",
        default=1, blank=True
    )

    def __str__(self):
        """
        Returns the string representation of the event.

        Returns:
            str: The title of the event.
        """
        return self.title
