from django.urls import path
from workoutsapp import views

urlpatterns = [
    path('', views.workouts, name="workouts"),
]