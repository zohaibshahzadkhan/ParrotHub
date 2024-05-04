from django.db import models
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class ParrotCategory(models.Model):
    """
    Stores a single parrot category entry.

    This model represents a category that can be assigned to a parrot.
    """

    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        """
        Returns the string representation of the ParrotCategory object.

        Returns:
          str: The name of the category.
        """
        return f"{self.name}"


class Parrot(models.Model):
    """
    Stores a single parrot entry related to :model:`parrots.parrot`.

    This model represents an individual parrot.
    """

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    characteristics = models.TextField()
    image = CloudinaryField("image", default="placeholder")
    about = models.TextField()
    category = models.ForeignKey(
        ParrotCategory, on_delete=models.CASCADE,
        related_name="parrot_category"
    )
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        """
        Returns the string representation of the Parrot object.
        Returns:
          str: The name of the parrot.
        """
        return f"{self.name}"
