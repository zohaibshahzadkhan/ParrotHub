from django.test import TestCase
from .models import Parrot, ParrotCategory


class ParrotModelTestCase(TestCase):
    def setUp(self):
        self.category = ParrotCategory.objects.create(name="Test Category")

        self.parrot = Parrot.objects.create(
            name="Test Parrot",
            slug="test-parrot",
            characteristics="Test Characteristics",
            image="test_image.jpg",
            about="Test About",
            category=self.category,
            status=1,
        )

    def test_parrot_model_fields(self):
        # Test the fields of the Parrot model
        self.assertEqual(self.parrot.name, "Test Parrot")
        self.assertEqual(self.parrot.slug, "test-parrot")
        self.assertEqual(self.parrot.characteristics, "Test Characteristics")
        self.assertEqual(self.parrot.image, "test_image.jpg")
        self.assertEqual(self.parrot.about, "Test About")
        self.assertEqual(self.parrot.category, self.category)
        self.assertEqual(self.parrot.status, 1)

    def test_parrot_str_representation(self):
        # Test the string representation of the Parrot model
        self.assertEqual(str(self.parrot), "Test Parrot")
