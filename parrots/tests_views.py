from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Parrot, ParrotCategory

class ParrotViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category1 = ParrotCategory.objects.create(name='Category 1')
        self.category2 = ParrotCategory.objects.create(name='Category 2')

        # Create test parrots
        self.parrot1 = Parrot.objects.create(
            name='Parrot 1',
            slug='parrot-1',
            characteristics='Characteristics of Parrot 1',
            about='About Parrot 1',
            category=self.category1,
            status=1
        )
        self.parrot2 = Parrot.objects.create(
            name='Parrot 2',
            slug='parrot-2',
            characteristics='Characteristics of Parrot 2',
            about='About Parrot 2',
            category=self.category2,
            status=1
        )

    def test_parrot_list_view(self):
        # Test parrot_list view
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parrots/index.html')
        self.assertIsInstance(
            response.context['parrots'], Parrot.objects.all().__class__)
        

    def test_parrot_detail_view(self):
        response = self.client.get(reverse('parrot_detail', args=['parrot-1']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parrots/parrot_detail.html')
        self.assertEqual(response.context['parrot'], self.parrot1)
