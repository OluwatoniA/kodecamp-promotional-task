from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.home,),
    path('hello/about/', views.about),
    path('hello/about/contact/', views.contact),
    
]