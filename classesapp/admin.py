from django.contrib import admin
from .models import Categoria, Clase

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
class ClaseAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Clase, ClaseAdmin)