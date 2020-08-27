from rest_framework import serializers
from .models import userProfile, AdvertiserProfile, PhaseDB


class userProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = userProfile
        fields = ('user_name',
                  'user_email',
                  'user_description',
                  'user_location',
                  'date_joined_for_user',
                  'user_profile_updated_on')
        extra_kwargs = {'user_password': {'write_only': True}}


class advertiserProfileSerializer(serializers.ModelSerializer):
    image_id = serializers.PrimaryKeyRelatedField(source="image_property_id", many=True, read_only=True)
    text_id = serializers.PrimaryKeyRelatedField(source="text_property_id", many=True, read_only=True)

    class Meta:
        model = AdvertiserProfile
        fields = ('advertiser_description',
                  'advertiser_location',
                  'date_joined_for_advertiser',
                  'advertiser_profile_updated_on',
                  'advertiser_is_organizer',
                  'advertiser_name',
                  'advertiser_password',
                  'advertiser_email',
                  'image_id',
                  'text_id')
        extra_kwargs = {'advertiser_password': {'write_only': True}}


class PhaseDBSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhaseDB
        fields = ('phase_id', 'phase_user_email', 'phase_advertiser_name', 'phase_position')
