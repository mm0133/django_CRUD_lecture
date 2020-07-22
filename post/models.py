from django.db import models

# Create your models here.


class Post(models.Model):

    title=models.CharField(max_length = 255, null=True)
    content=models.TextField(null=True)
    writer=models.CharField(max_length = 255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

