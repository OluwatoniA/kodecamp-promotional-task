from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'name':'Toni'})

def about(request):
    return render(request, 'about.html', {'about':'Male'})

def contact(request):
    return render(request, 'contact.html', {'contact':'08142312782'})
     



# Create your views here.
