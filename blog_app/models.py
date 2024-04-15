from django.db import models
from django.utils.text import slugify
from datetime import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=240)
    slug = models.SlugField(blank=True)
    date = models.DateTimeField(default=datetime.now())
    content = models.TextField()
    views = models.IntegerField()
    

    def save(self, *args, **kwargs) :
        self.slug  = slugify(self.title)
        return super().save(*args, **kwargs)