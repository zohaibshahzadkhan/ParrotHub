from django.shortcuts import render
from .models import Parrot

# Create your views here.

def parrot_list(request):
  parrots = Parrot.objects.filter(status=1)

  return render(
    request,
    "parrots/index.html",
    {
      "parrots": parrots
    }
  )
