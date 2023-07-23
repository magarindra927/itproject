from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    data={
        'foodData':Food.objects.all()
    }
    return render(request, 'index.html', data)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def food(request, slug):
    data={
        'fodData':Food.objects.get(slug=slug),
    }
    return render(request, 'food.html', data)

def variety(request,slug):
    var=Variety.objects.get(slug=slug)
    food=var.food.id
    related_items=Variety.objects.filter(food=food).exclude(id=var.id)
    data={
        'var':Variety.objects.get(slug=slug),
        'related_items':related_items,
    }
    return render(request, 'variety.html', data)

 