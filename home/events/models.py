from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.CharField(max_length=50)
    slug = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(blank=True)

    # category = models.CharField(max_length=50)    

    def __str__(self):
        return self.title 
        # + ' by ' + self.author