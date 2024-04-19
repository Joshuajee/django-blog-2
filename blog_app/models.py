from django.db import models
from django.utils.text import slugify
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    location = models.CharField(max_length=100)
    profile_img = models.FileField(upload_to="profiles", blank=True)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=240)
    slug = models.SlugField(blank=True)
    date = models.DateTimeField(default=datetime.now())
    content = models.TextField()
    views = models.IntegerField()
    

    def save(self, *args, **kwargs) :
        self.slug  = slugify(self.title)
        return super().save(*args, **kwargs)