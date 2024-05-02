from . import views
from django.urls import path
from .views import add_event, delete_event

urlpatterns = [ 
  path("", views.event_list, name="events"),
  path('add/', add_event, name='add_event'),
  path('delete/<int:event_id>', delete_event, name='delete_event')
]