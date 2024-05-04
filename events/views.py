from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Event
from .forms import EventForm


def event_list(request):
  """
    Renders a list of events with a status of 'Published' and renders them 
    in the events template.
    Display an individual instance of :model:`events.Event`
    **Context**
    ``events``
      list of events with a status of 'Published' :model:`events.Event`
    **Template:**
    :template:events/events.html

    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered template with the list of events obtained from the database.
  """
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
  """
    Add an event.
    Allows staff users to add a new event. If the form is valid, the event 
    will be saved and a success message will be displayed. 
    If the form is not valid, the add event form will be displayed.
    **Context**
    ``event_form``
      An instance of form  :from:`events.EventForm`
    **Template:**
    :template:events/add_event.html

    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered template with the add event form.
  """
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
  """
    Delete an event.
    Allows staff users to delete an existing event. If the event is found, 
    it will be deleted and a success message will be displayed.

    Args:
        request (HttpRequest): The HTTP request object.
        event_id (int): The ID of the event to be deleted.
    Returns:
        HttpResponse: Redirects to the events list page.
  """
  event = get_object_or_404(Event, id=event_id)
  if request.method == 'POST':
    event.delete()
    messages.add_message(request, messages.SUCCESS, 'Event deleted!')
    return redirect('events')

@staff_member_required
def update_event(request, event_id):
  """
  Update an event.
  Allows staff users to update an existing event. If the form is valid, 
  the event will be updated and a success message will be displayed.

  Args:
    request (HttpRequest): The HTTP request object.
    event_id (int): The ID of the event to be updated.
  Returns:
    HttpResponse: Redirects to the events list page.
  """
  event = get_object_or_404(Event, id=event_id)
  if request.method == 'POST':
    event_form = EventForm(data=request.POST, instance=event)
    if event_form.is_valid():
      event_form.save()
      messages.add_message(request, messages.SUCCESS, 'Event Updated!')
      return redirect('events')