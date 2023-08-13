from django.shortcuts import render, HttpResponse
from .models import Burgers

# Create your views here.

def home(request):
    #return HttpResponse("Burger Shop")
    return render(request, "home.html")

def burgers(request):
    items = Burgers.objects.all()
    return render(request, "burgers.html", {"todos":items})
