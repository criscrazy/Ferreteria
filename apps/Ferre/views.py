from django.shortcuts import render
from .models import *

def index(request):
    allproduct = producto.objects.all()
    return render(request, 'index.html', {'allproduct':allproduct})

def contact(request):
    return render(request, 'contact.html')
# Create your views here.

