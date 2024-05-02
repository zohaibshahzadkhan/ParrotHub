from django.shortcuts import render, get_object_or_404
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

def parrot_detail(request, slug):
   queryset = Parrot.objects.filter(status=1)
   parrot = get_object_or_404(queryset, slug=slug)

   return render(
      request,
      "parrots/parrot_detail.html",
      {
        "parrot": parrot,         
      },
    )
