from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import userProfile,CompanyProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer,companyProfileSerializer

# Create your views here.

class UserProfileListCreateView(ListCreateAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

class CompanyProfileListCreateView(ListCreateAPIView):
    queryset=CompanyProfile.objects.all()
    serializer_class=companyProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        company_val=self.request.company
        serializer.save(company=company_val)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]

class companyProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=userProfile.objects.all()
    serializer_class=companyProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]