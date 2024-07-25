from django.urls import path
from contactapp import views

urlpatterns = [
    path('', views.contact, name="contact"),
]