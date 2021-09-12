from django.shortcuts import render
from .models import*
from .forms import*
# Create your views here.

def info(request):
    cards=Staff.objects.all()
    context={'cards':cards}


    return render(request,'index.html',context)

def form(request):
    return render(request,'form.html')

def Tashish(request):
    return render(request,'index.html')

def tabel(request):
    tabel=Tabel.objects.all()
    context={'tabel':tabel}
    return render(request,'tabel.html',context)
# tabel Filter

