# from tkinter import CASCADE
from django.db import models

# Create your models here.

# class User(models.Model):
#     username = models.CharField(max_length=50)
#     user_fname = models.CharField(max_length=40)
#     user_lname = models.CharField(max_length=40)
#     user_email = models.EmailField()

#     def __str__(self):
#         return self.username

# class Post(models.Model):
#     form_title = models.CharField(max_length=1000)
#     form_content = models.CharField(max_length=10000)
#     time_stamp = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.form_title

# class Profile(models.Model):
#     age = models.CharField(max_length=10)
#     bio = models.CharField(max_length=1000)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.bio
