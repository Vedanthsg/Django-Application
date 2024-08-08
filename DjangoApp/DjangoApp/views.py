from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello Everyone Its A Django App Home Page")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello Everyone Its A Django App About Page")
    return render(request , 'website/about.html')

def contact(request):
    # return HttpResponse("Hello Everyone Its A Django App Contact Page")
    return render(request, 'website/contact.html')
