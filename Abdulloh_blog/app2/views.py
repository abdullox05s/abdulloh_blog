from django.shortcuts import render

from .models import *


def index (request):
    data={
        "Home":Home.objects.all(),
        "About":About_me.objects.all(),
        "My_image":My_images.objects.all(),
        "My_life":My_life.objects.all(),
        'My_achivments':My_achchivements.objects.all(),
        'My_future':My_status_for_future.objects.all(),
        "My_portfolio":My_portfolio.objects.all(),
        "Surprising":Surprising_situations.objects.all(),

    }
    return render(request,'index.html',data)


def portfolio_detail(request,a):
    data={
        'Portfolio':My_portfolio.objects.get(id=a)
    }
    return render(request,'portfolio-details.html',data)

def single(request, a):
    data={
        "Event":Home.objects.get(id=a)
    }
    return render(request,'single.html',data)

def mission_single(request, a):
    data={
        "Mission":My_status_for_future.objects.get(id=a)
    }
    return render(request,'misson-single.html',data)

def my_life(request,a):
    print("==========================",My_life.objects.get(id=a))
    data={
        "My_life":My_life.objects.get(id=a)
    }
    return render(request,'my_life.html',data)