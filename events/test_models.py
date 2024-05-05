from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date, time, timedelta
from .models import Event


class EventModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="test_user",
            password="password"
        )
        cls.event = Event.objects.create(
            title="Test Event",
            description="Test Description",
            date=date.today(),
            time=time(hour=12, minute=0),
            location="Test Location",
            status=1,
            author=cls.user,
        )

    def test_event_str_method(self):
        """
        Test the __str__ method of the Event model.
        """
        self.assertEqual(str(self.event), "Test Event")

    def test_event_created_on_auto_now_add(self):
        """
        Test if the created_on field is automatically
        set to the current timestamp.
        """
        created_on_value = self.event.created_on
        self.assertIsNotNone(created_on_value)
        self.assertAlmostEqual(
            created_on_value, timezone.now(), delta=timedelta(seconds=5)
        )
