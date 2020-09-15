from rest_framework.permissions import IsAuthenticated
from .models import userProfile, AdvertiserProfile, PhaseDB
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer, advertiserProfileSerializer, PhaseDBSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from logger_settings import api_logger


# Create your views here.   `

class UserView(APIView):
    serializer_class = userProfileSerializer

    # permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            all_user_data = userProfile.objects.all()
            serializer = userProfileSerializer(all_user_data, many=True)
            api_logger.info("Retrieving user data...")
            api_logger.info("User_data: " + str(serializer.data))
            return Response(serializer.data)

        except Exception as e:
            api_logger.exception("Failure in retrieving user data...", str(e))

    def post(self, request, *args, **kwargs):
        try:
            serializer = userProfileSerializer(data=request.data)
            if serializer.is_valid():
                user_data = serializer.save()
                serializer = userProfileSerializer(user_data)
                api_logger.info("User_data: " + str(serializer.data))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                api_logger.error("Error in user data..." + str(serializer.errors))
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            api_logger.exception(str(e))



class AdvertiserView(APIView):
    serializer_class = advertiserProfileSerializer

    # permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            all_advertiser_data = AdvertiserProfile.objects.all()
            serializer = advertiserProfileSerializer(all_advertiser_data, many=True)
            api_logger.info("Retrieving advertiser data...")
            api_logger.info("Advertiser data..."+str(serializer.data))
            return Response(serializer.data)

        except Exception as e:
            api_logger.exception("Unable to retrieve advertiser data..."+str(e))

    def post(self, request, *args, **kwargs):
        try:
            serializer = advertiserProfileSerializer(data=request.data)
            if serializer.is_valid():
                advertiser_data = serializer.save()
                serializer = advertiserProfileSerializer(advertiser_data)
                api_logger.info("Advertiser profile: " + str(serializer.data))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                api_logger.error("Advertiser profile: " + str(serializer.data))
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            api_logger.exception(str(e))



class PhaseView(APIView):
    serializer_class = PhaseDBSerializer

    def get(self, request, *args, **kwargs):
        try:
            all_phase_data = PhaseDB.objects.all()
            serializer = PhaseDBSerializer(all_phase_data, many=True)
            api_logger.info("Phase profile data: " + str(serializer.data))
            return Response(serializer.data)

        except Exception as e:
            api_logger.exception("Error in retrieving phase data..."+str(e))
