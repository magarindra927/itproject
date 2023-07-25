from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api', views.VarietyViewSet)




urlpatterns=[
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('food/<slug>', views.food, name='food'),
    path('variety/<slug>', views.variety, name='variety'),
    path('variety_food', views.variety_food, name='variety_food'),
    path('category/<slug>', views.category, name='category'),
    path('api/', include(router.urls)),
    path('news_api', views.news_api, name='news_api')
]