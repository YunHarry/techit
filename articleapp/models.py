from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    image = models.ImageField(upload_to='article/', null=False)
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(null=True)

    like = models.IntegerField(default=0)

    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)