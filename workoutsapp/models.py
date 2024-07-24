from django.db import models

# Create your models here.

class Workout(models.Model):
    name = models.CharField(max_length=50)
    muscle = models.CharField(max_length=50)
    image = models.ImageField(upload_to='workouts')
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'workout'
        verbose_name_plural = 'workouts'
        
    def __str__(self):
        return self.name