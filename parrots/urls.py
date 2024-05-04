from django.urls import path
from . import views


urlpatterns = [
    path("", views.parrot_list, name="home"),
    path("<slug:slug>/", views.parrot_detail, name="parrot_detail"),
]
