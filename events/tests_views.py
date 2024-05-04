from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Event
from datetime import date, time

class EventsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.staff_user = User.objects.create_user(username='staffuser', password='staffpassword', is_staff=True)
        self.event = Event.objects.create(
            title='Test Event',
            description='Test Description',
            date=date.today(),
            time=time(hour=12, minute=0),
            status=1
        )

    def test_event_list_view(self):
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events.html')
        self.assertIsInstance(
            response.context['events'], Event.objects.all().__class__)
        

    def test_add_event_view_authenticated(self):
        self.client.login(username='staffuser', password='staffpassword')
        post_data = {
            'title': 'New Test Event',
            'description': 'New Test Description',
            'date': '2024-05-04',
            'time': '12:00',
            'location': 'New Test Location',
            'status': 1
        }
        response = self.client.post(reverse('add_event'),post_data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Event.objects.count(), 2)
        self.assertRedirects(response, reverse('events'))

    def test_delete_event_view_authenticated(self):
        self.client.login(username='staffuser', password='staffpassword')
        response = self.client.post(reverse('delete_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Event.objects.count(), 0)
        self.assertRedirects(response, reverse('events'))

    def test_update_event_view_authenticated(self):
        self.client.login(username='staffuser', password='staffpassword')
        updated_title = 'Updated Test Event'
        response = self.client.post(reverse('update_event', args=[self.event.id]), {
            'title': updated_title,
            'description': 'Updated Test Description',
            'date': '2024-05-04',
            'time': '12:00',
            'location': 'Updated Test Location',
            'status': 1
        })
        self.assertEqual(response.status_code, 302)
        self.event.refresh_from_db()
        self.assertEqual(self.event.title, updated_title)
        self.assertRedirects(response, reverse('events'))
