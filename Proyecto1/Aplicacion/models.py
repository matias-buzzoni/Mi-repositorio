from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario (models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.title

