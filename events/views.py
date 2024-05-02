from django.shortcuts import render
from .models import Event


def event_list(request):
  events = Event.objects.filter(status=1)

  return render(
    request,
    "events/events.html",
    {
      "events": events
    }
  )