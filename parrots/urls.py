from . import views
from django.urls import path

urlpatterns = [ 
  path("", views.parrot_list, name="home")
]