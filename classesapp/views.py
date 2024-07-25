from django.shortcuts import render
from .models import Clase, Categoria

# Create your views here.

def classes(request):

    clases = Clase.objects.all()
    categorias = Categoria.objects.all()
    
    return render(request, 'classesapp/classes.html', {'clases':clases, 'categorias':categorias})


def categoria(request, categoria_id):
    
    categoria = Categoria.objects.get(id=categoria_id)
    clases = Clase.objects.filter(categorias = categoria)
    
    return render(request, 'classesapp/categorias.html', {'categoria':categoria,'clases':clases})