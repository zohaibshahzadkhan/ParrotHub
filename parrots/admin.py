from django.contrib import admin
from .models import Parrot, ParrotCategory

# Register your models here.
admin.site.register(Parrot),
admin.site.register(ParrotCategory)
