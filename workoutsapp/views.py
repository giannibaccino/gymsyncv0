from django.shortcuts import render
from .models import Workout

# Create your views here.

def workouts(request):
    
    workouts = Workout.objects.all()

    return render(request, 'workoutsapp/workouts.html', {'workouts': workouts})


