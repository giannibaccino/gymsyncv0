from django.urls import path
from gymsyncapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('stats/', views.stats, name="stats"),
]