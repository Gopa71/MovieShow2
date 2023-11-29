from django.shortcuts import render
from .models import Movies

# Create your views here.
def home(req):
    obj=Movies.objects.all
    return render(req,'index.html',{'Movies':obj})
def more(req):
    return render(req,'more.html')