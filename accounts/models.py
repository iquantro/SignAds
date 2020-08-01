from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_description = models.TextField(blank=True, null=True)
    user_location = models.CharField(max_length=30, blank=True)
    date_joined_for_user = models.DateTimeField(auto_now_add=True)
    user_profile_updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username

class AdvertiserProfile(models.Model):
    date_joined_for_advertiser = models.DateTimeField(auto_now_add=True)
    advertiser_profile_updated_on = models.DateTimeField(auto_now=True)
    advertiser_is_organizer = models.BooleanField(default=False)
    advertiser_location = models.CharField(max_length=30, blank=True)
    advertiser_description = models.TextField(blank=True, null=True)
    advertiser = models.OneToOneField(User, on_delete=models.CASCADE)