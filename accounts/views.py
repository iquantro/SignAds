from rest_framework.permissions import IsAuthenticated
from .models import userProfile, AdvertiserProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer, advertiserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserView(APIView):
    serializer_class = userProfileSerializer

    #permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def get(self, request, *args, **kwargs):
        all_user_data = userProfile.objects.all()
        serializer = userProfileSerializer(all_user_data, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = userProfileSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.save()
            serializer = userProfileSerializer(user_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdvertiserView(APIView):
    serializer_class = advertiserProfileSerializer
    #permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def get(self, request, *args, **kwargs):
        all_advertiser_data = AdvertiserProfile.objects.all()
        serializer = advertiserProfileSerializer(all_advertiser_data, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = advertiserProfileSerializer(data=request.data)
        if serializer.is_valid():
            advertiser_data = serializer.save()
            serializer = advertiserProfileSerializer(advertiser_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
