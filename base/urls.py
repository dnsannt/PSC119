from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('index2', views.index2, name='index2'),
    path('index3', views.index3, name='index3'),
]
