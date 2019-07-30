from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Blog(models.Model):
    blogger = models.ForeignKey(User, on_delete=models.CASCADE, default="5") #, blank=True, null=True
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
