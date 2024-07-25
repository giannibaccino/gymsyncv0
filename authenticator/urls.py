from django.urls import path
from authenticator import views

urlpatterns = [
    path('', views.auth, name="auth"),
]