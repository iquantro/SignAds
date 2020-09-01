from django.db import models
# Create your models here.


class userProfile(models.Model):
    user_name = models.CharField(max_length=30, blank=True)
    user_password = models.CharField(max_length=30, blank=False)
    user_email = models.CharField(max_length=30, blank=False)
    user_description = models.TextField(blank=True, null=True)
    user_location = models.CharField(max_length=30, blank=True)
    date_joined_for_user = models.DateTimeField(auto_now_add=True)
    user_profile_updated_on = models.DateTimeField(auto_now=True)

class AdvertiserProfile(models.Model):
    date_joined_for_advertiser = models.DateTimeField(auto_now_add=True)
    advertiser_profile_updated_on = models.DateTimeField(auto_now=True)
    advertiser_is_organizer = models.BooleanField(default=False)
    advertiser_location = models.CharField(max_length=30, blank=True)
    advertiser_description = models.TextField(blank=True, null=True)
    advertiser_name = models.CharField(max_length=30, blank=False)
    advertiser_password = models.CharField(max_length=30, blank=False)
    advertiser_email = models.CharField(max_length=30, blank=True)

class PhaseDB(models.Model):
    phase_id = models.IntegerField(blank=False, default=1)
    phase_position = models.CharField(max_length=30, blank=False)
    phase_user_email = models.CharField(max_length=30, blank=False)
    phase_advertiser_name = models.CharField(max_length=30, blank=False)