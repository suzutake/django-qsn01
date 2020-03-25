from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def showIndex(request):
    return render(request, 'index.html')
