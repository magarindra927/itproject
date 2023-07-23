from django.urls import path, include
from .import views

urlpatterns=[
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('food/<slug>', views.food, name='food'),
    path('variety/<slug>', views.variety, name='variety')
]