from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages

from rest_framework import viewsets
from .serializers import VarietySerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

import requests;

class VarietyViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer




# Create your views here.

def index(request):
    data={
        'foodData':Food.objects.all()
    }
    return render(request, 'index.html', data)

def contact(request):
    if request.method == 'POST':
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        send_mail("Subject:" + subject, message, email,['magarindra927@gmail.com'], fail_silently=False)
        messages.success(request, 'Your message has been sent successfully')
        back=request.META.get('HTTP_REFERER')
        return redirect(back)
    else:
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


def variety_food(request):
    if request.method=='POST':
        Search=request.POST['search']
        find_data=Variety.objects.filter(food__name__icontains=Search) 
        paginator = Paginator(variety_data, 6) 
        page = request.GET.get('page')
        variety_data = paginator.get_page(page)
        data={
            'allfood':find_data,
        }
        return render(request, 'variety_food.html', data)
    else:
        variety_data=Variety.objects.all()
        paginator = Paginator(variety_data, 6) 
        page = request.GET.get('page')
        variety_data = paginator.get_page(page)
        data={
            'allfood':variety_data,
        }
    return render(request, 'variety_food.html', data)    

def category(request, slug):
    data={
        'cat':Category.objects.get(slug=slug)
    }
    return render(request, 'category.html', data) 



def news_api(request):
    url="https://newsapi.org/v2/everything?q=tesla&from=2023-06-25&sortBy=publishedAt&apiKey=d9ee7c42051e40ffa298114b256596fa"    
    response=requests.get(url)
    data=response.json()
    data=data['articles']
    send_data={
        'allfood':data
    }
    return render(request, 'api.html', send_data)
