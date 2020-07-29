from rest_framework import serializers
from .models import userProfile,CompanyProfile




class userProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)

    class Meta:
        model=userProfile
        fields='__all__'

class companyProfileSerializer(serializers.ModelSerializer):
    company=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=CompanyProfile
        fields='__all__'