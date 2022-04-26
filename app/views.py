from django.shortcuts import render
from .models import Idcard

# Create your views here.
def index(request):  
    cards = Idcard.objects.all()
    return render(request, 'index.html',{'cards':cards})