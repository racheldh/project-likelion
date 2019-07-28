from django.db import models
from django.utils import timezone

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(default = timezone.now)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title
    def summary(self):
        return self.description[:100]

class Comment(models.Model):
    portfolio = models.ForeignKey('portfolio.Portfolio', related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.text