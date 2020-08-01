from rest_framework import serializers
from .models import userProfile, AdvertiserProfile




class userProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model=userProfile
        fields=('user',
                  'user_description',
                  'user_location',
                  'date_joined_for_user',
                  'user_profile_updated_on',
                  'user_is_organizer')

class advertiserProfileSerializer(serializers.ModelSerializer):
    advertiser = serializers.StringRelatedField(read_only=True)
    image_id = serializers.PrimaryKeyRelatedField(source="image_property_id", many=True, read_only=True)
    text_id = serializers.PrimaryKeyRelatedField(source="text_property_id", many=True, read_only=True)

    class Meta:
        model = AdvertiserProfile
        fields=('advertiser',
                  'advertiser_description',
                  'advertiser_location',
                  'date_joined_for_advertiser',
                  'advertiser_profile_updated_on',
                  'advertiser_is_organizer',
                  'image_id',
                  'text_id')