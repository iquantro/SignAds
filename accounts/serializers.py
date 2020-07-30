from rest_framework import serializers
from .models import userProfile,CompanyProfile




class userProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    image_id = serializers.PrimaryKeyRelatedField(source="image_property_id", many=True, read_only=True)
    text_id = serializers.PrimaryKeyRelatedField(source="text_property_id", many=True, read_only=True)

    class Meta:
        model=userProfile
        fields=('user',
                  'user_description',
                  'user_location',
                  'date_joined_for_user',
                  'user_profile_updated_on',
                  'user_is_organizer',
                  'image_id',
                  'text_id')

class companyProfileSerializer(serializers.ModelSerializer):
    company=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=CompanyProfile
        fields='__all__'