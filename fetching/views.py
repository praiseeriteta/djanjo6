from django.shortcuts import render
from .models import Django6
# Create your views here.

def home(request):
    name = "paige"
    age = 45
    return render(request, "house/home.html")
def about(request):
    return render(request, "house/about.html")
def contact(request):
    return render(request, "house/contact.html")
def blog(request):
    post =Django6.objects.all()
    return render(request, "house/blog.html",{'post':post})
def talk(request):
    return render(request, "house/talk.html")