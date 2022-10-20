from enum import auto
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Music(models.Model): 
    siger = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    audio = models.FileField()
    image = models.ImageField(upload_to='music/', blank=True)

    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']