from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        
    def __str__(self):
        return self.nombre
    
    
class Clase(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    image = models.ImageField(upload_to='classes', null=True, blank=True)
    autor = models.ForeignKey(User,on_delete=models.CASCADE,)
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'clase'
        verbose_name_plural = 'clases'
        
    def __str__(self):
        return self.titulo