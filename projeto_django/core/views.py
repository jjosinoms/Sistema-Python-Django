from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
def contact(request):
    return render(request, 'contact.html')
def base(request):
    return render(request, 'base.html')
