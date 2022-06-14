
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Info(models.Model):
    post_title = models.CharField(max_length=1000)
    post_content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title 

    def snippet(self):
        return self.post_content[:10] + "..."