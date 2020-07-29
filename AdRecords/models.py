from django.db import models
from accounts.models import userProfile

class Image(models.Model):
    image = models.FileField(blank=False, null=False)
    image_description = models.CharField(max_length=255)
    image_uploaded_at = models.DateTimeField(auto_now_add=True)
    image_property_id = models.ForeignKey(userProfile, null=False, on_delete=models.CASCADE)

class Text(models.Model):
    text = models.CharField(max_length=300)
    text_uploaded_at = models.DateTimeField(auto_now_add=True)
    text_description = models.CharField(max_length=255)
    text_property_id = models.ForeignKey(userProfile, null=False, on_delete=models.CASCADE)