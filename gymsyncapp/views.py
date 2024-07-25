from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, 'gymsyncapp/home.html')


def stats(request):

    return render(request, 'gymsyncapp/stats.html')


def shop(request):

    return render(request, 'gymsyncapp/shop.html')