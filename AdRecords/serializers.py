from rest_framework import serializers
from .models import Image,Text

class ImageSerializer(serializers.ModelSerializer):
    class Meta():
        model = Image
        fields = (
            'image_property_id',
            'image'
        )

class TextSerializer(serializers.ModelSerializer):
    class Meta():
        model = Text
        fields = (
            'text_property_id',
            'text'
        )