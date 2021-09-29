from django.shortcuts import render
from .models import *

def index(request):
    allproduct = producto.objects.all()
    return render(request, 'index.html', {'allproduct':allproduct})
# Create your views here.
