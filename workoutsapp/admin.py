from django.contrib import admin
from .models import Workout

# Register your models here.

class WorkoutAdmin(admin.ModelAdmin):
    readonly_fields=('date',)

admin.site.register(Workout, WorkoutAdmin)