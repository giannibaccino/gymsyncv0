from django.urls import path
from classesapp import views

urlpatterns = [
    path('', views.classes, name="classes"),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
]