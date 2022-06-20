from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(max_length=2000)

"""
    Those will be a pictures for posts 
class Images(models.Model):
    name = models.CharField()
    picture = models.ImageField
"""
