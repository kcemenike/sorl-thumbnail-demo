from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    image = ImageField(upload_to="%Y/%m/%d/", blank=True, max_length=200)
