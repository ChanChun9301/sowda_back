from django.shortcuts import render
from logist.models import *
from other.models import *
from service.models import *
from elin.models import *
from car.models import *
from .models import *
from .functions import hash_password
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

def index(request):
    user = UserProd.objects.get(username=request.user.username)
    token,created =Token.objects.get_or_create(user=user)
    logist = Logist.objects.all()[:8]
    car = Car.objects.all()[:8]
    other = Other.objects.all()[:8]
    news = News.objects.all()[:8]
    service = Service.objects.all()[:8]
    elin = Elin.objects.all()[:8]   
    context = {
        'car':car,
        'logist':logist,
        'elin':elin,
        'other':other,
        'service':service,
        'news':news,
        'token':token
    }
    return render(request,'index.html',context)

def logist(request):
    logist = Logist.objects.all()
    context = {
        'logist':logist,
    }
    return render(request,'logist.html',context)

def logist_detail(request,pk):
    logist = Logist.objects.get(pk=pk)
    images = ImageLogist.objects.filter(logist__pk=pk)
    context = {
        'logist':logist,
        'images':images,
    }
    print(images)
    return render(request,'logist_detail.html',context)

def car(request):
    car = Car.objects.all()
    context = {
        'car':car,
    }
    return render(request,'car.html',context)

def car_detail(request,pk):
    car = Car.objects.get(pk=pk)
    context = {
        'car':car,
    }
    return render(request,'car_detail.html',context)

def elin(request):
    elin = Elin.objects.all()
    context = {
        'elin':elin,
    }
    return render(request,'elin.html',context)

def elin_detail(request,pk):
    elin = Elin.objects.get(pk=pk)
    context = {
        'elin':elin,
    }
    return render(request,'elin_detail.html',context)

def service(request):
    service = Service.objects.all()
    context = {
        'service':service,
    }
    return render(request,'service.html',context)

def service_detail(request,pk):
    service = Service.objects.get(pk=pk)
    context = {
        'service':service,
    }
    return render(request,'service_detail.html',context)

def other(request):
    other = Other.objects.all()
    context = {
        'other':other,
    }
    return render(request,'other.html',context)

def other_detail(request,pk):
    other = Other.objects.get(pk=pk)
    context = {
        'other':other,
    }
    return render(request,'other_detail.html',context)

def news(request):
    news = News.objects.all()
    context = {
        'news':news,
    }
    return render(request,'news.html',context)

def news_detail(request,pk):
    news = News.objects.get(pk=pk)
    context = {
        'news':news,
    }
    return render(request,'news_detail.html',context)