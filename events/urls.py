from . import views
from django.urls import path

urlpatterns = [ 
  path("", views.event_list, name="events"),
]