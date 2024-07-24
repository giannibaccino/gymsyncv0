from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, 'gymsyncapp/home.html')


def classes(request):

    return render(request, 'gymsyncapp/classes.html')


def stats(request):

    return render(request, 'gymsyncapp/stats.html')