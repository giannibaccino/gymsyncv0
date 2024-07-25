from django.shortcuts import render
from .kart import Kart
from shopapp.models import Producto
from django.shortcuts import redirect

# Create your views here.

def add_prod(request, product_id):
    
    kart = Kart(request)
    product = Producto.objects.get(id=product_id)
    kart.add_prod(producto=product)
    
    return redirect('shop')

def delete_prod(request, product_id):
    
    kart = Kart(request)
    product = Producto.objects.get(id=product_id)
    kart.delete_prod(producto=product)
    
    return redirect('shop')

def remove_prod(request, product_id):
    
    kart = Kart(request)
    product = Producto.objects.get(id=product_id)
    kart.remove_prod(producto=product)
    
    return redirect('shop')

def clean_kart(request):
    
    kart = Kart(request)
    kart.empty_kart()
    
    return redirect('shop')