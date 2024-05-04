from django.shortcuts import render, get_object_or_404
from .models import Parrot


def parrot_list(request):
  """
    Render the parrot list page.
    Retrieves a list of parrots with status set to 'Published' from the database.
    **Context**
    ``parrot``
      list of parrots with a status of 'Published' :model:`parrots.Parrot`
    **Template:**
    :template:parrots/index.html

    Args:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: The rendered HTML page displaying the list of parrots.
  """
  parrots = Parrot.objects.filter(status=1)
  return render(
    request,
    "parrots/index.html",
    {
      "parrots": parrots
    }
  )

def parrot_detail(request, slug):
  """
    Render the parrot detail page.
    This view retrieves a single parrot with the given slug and status set to 'Published' from the database
    **Context**
    ``parrot``
      individual parrot with a status of 'Published' :model:`parrots.Parrot`
    **Template:**
    :template:parrots/parrot_detail.html

    Args:
        request (HttpRequest): The request object sent by the client.
        slug (str): The unique slug of the parrot to be displayed.
    Returns:
        HttpResponse: The rendered HTML page displaying the details of the specified parrot.
  """
  queryset = Parrot.objects.filter(status=1)
  parrot = get_object_or_404(queryset, slug=slug)

  return render(
      request,
      "parrots/parrot_detail.html",
      {
        "parrot": parrot,         
      },
    )
