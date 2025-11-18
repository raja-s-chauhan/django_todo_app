from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to the Todo App Home Page!")
    return render(request, 'home.html')