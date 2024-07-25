from django.urls import path
from kartapp import views

app_name = 'kart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_prod, name="add_prod"),
    path('remove/<int:product_id>/', views.remove_prod, name="remove_prod"),
    path('delete/<int:product_id>/', views.delete_prod, name="delete_prod"),
    path('clean/', views.clean_kart, name="clean_kart"),
]