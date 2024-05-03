from django.test import TestCase
from datetime import date, time
from .forms import EventForm

class EventFormTest(TestCase):
    def test_event_form_valid(self):
        """
        Test that the form is valid with valid data.
        """
        form_data = {
            'title': 'Test Event',
            'description': 'This is a test event',
            'date': date(2024, 5, 4),
            'time': time(10, 0),
            'location': 'Test Location',
            'status': 1
        }
        form = EventForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_event_form_invalid(self):
        """
        Test that the form is invalid with missing required data.
        """
        form_data = {
            'title': '',  # Title is required
            'description': 'This is a test event',
            'date': date(2024, 5, 4),
            'time': time(10, 0),
            'location': 'Test Location',
            'status': 1
        }
        form = EventForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_max_length_validation(self):
        """
        Test that the form is invalid when the title field exceeds the maximum length.
        """
        max_length = 200
        long_title = 'a' * (max_length + 1)
        form_data = {
            'title': long_title,
            'description': 'This is a test event',
            'date': date(2024, 5, 4),
            'time': time(10, 0),
            'location': 'Test Location',
            'status': 1
        }
        form = EventForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_invalid_choices_validation(self):
        """
        Test that the form is invalid when an invalid choice for the status field is provided.
        """
        invalid_status = 999  # Invalid status value
        form_data = {
            'title': 'Test Event',
            'description': 'This is a test event',
            'date': date(2024, 5, 4),
            'time': time(10, 0),
            'location': 'Test Location',
            'status': invalid_status
        }
        form = EventForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('status', form.errors)
    
    def test_valid_choices_validation(self):
      """
      Test that the form is valid when a valid choice for the status field is provided.
      """
      valid_status = 0  # Valid status value
      form_data = {
        'title': 'Test Event',
        'description': 'This is a test event',
        'date': date(2024, 5, 4),
        'time': time(10, 0),
        'location': 'Test Location',
        'status': valid_status
      }
      form = EventForm(data=form_data)
      self.assertTrue(form.is_valid())
      self.assertNotIn('status', form.errors)

    
    

