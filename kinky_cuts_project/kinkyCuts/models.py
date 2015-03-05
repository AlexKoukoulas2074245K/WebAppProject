from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profilepic = models.ImageField(upload_to='profile_images', blank=True)
    

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.user.username

class Creation(models.Model):
    user = models.ForeignKey(User)
    imageID = models.IntegerField(default=0, unique=True)
    favourites = models.ImageField(upload_to='pictures', blank=True)
    def __unicode__(self):
        return self.user.username


class Rating(models.Model):
     #whats needed
    user = models.ForeignKey(User)
    Creation = models.ForeignKey(Creation)
    
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.user.username

