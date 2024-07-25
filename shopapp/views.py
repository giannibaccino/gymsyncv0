from django.shortcuts import render
from .models import Producto,Categoria

# Create your views here.

def shop(request):
    
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    
    return render(request, 'shopapp/shop.html', {'productos':productos,'categorias':categorias})