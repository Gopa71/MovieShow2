from django.shortcuts import render
from .models import Movies
from .models import Promo

# Create your views here.
def home(req):
    obj=Movies.objects.all
    obj1=Promo.objects.all
    return render(req,'index.html',{'Movies':obj,'Promo':obj1})
def more(req):
    return render(req,'more.html')