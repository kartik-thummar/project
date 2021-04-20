from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# from .forms import PostForm

class Category(models.Model):
    cat_name = models.CharField(max_length=50)

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        # return reverse("eventpost", args=str(self.sno))
        return reverse('events')
    

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, default='Uncategarised')
    content = models.TextField()
    # author = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    timeStamp = models.DateField(auto_now_add=True)
    # timeStamp = models.DateTimeField(auto_now=False, auto_now_add=True)
        
    def __str__(self):
        return self.title + ' by ' + str(self.author)

    def get_absolute_url(self):
        # return reverse("eventpost", args=(self.slug))
        return reverse("events")
    