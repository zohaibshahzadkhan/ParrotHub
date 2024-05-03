from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Event
from .forms import EventForm


def event_list(request):
  events = Event.objects.filter(status=1)

  return render(
    request,
    "events/events.html",
    {
      "events": events
    }
  )

@staff_member_required
def add_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            messages.add_message(request, messages.SUCCESS, "Event has been added successfully!")
            return redirect('events')  
    else:
        event_form = EventForm()
    return render(
        request, 
        'events/add_event.html', 
        {
            'event_form': event_form
        }
      )

@staff_member_required
def delete_event(request,event_id):
     event = get_object_or_404(Event, id=event_id)
     if request.method == 'POST':
        event.delete()
        messages.add_message(request, messages.SUCCESS, 'Event deleted!')
        return redirect('events')

@staff_member_required
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event_form = EventForm(data=request.POST, instance=event)

        if event_form.is_valid():
            event_form.save()
            messages.add_message(request, messages.SUCCESS, 'Event Updated!')
            return redirect('events')