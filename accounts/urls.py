from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileListCreateView, userProfileDetailView
from .views import CompanyProfileListCreateView,companyProfileDetailView

urlpatterns = [
    #gets all user profiles and create a new profile
    path("all-user-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
   # retrieves profile details of the currently logged in user
    path("user-profile/<int:pk>",userProfileDetailView.as_view(),name="profile"),

    #gets all customer profiles and creates a new customer
    path("all-company-profiles",CompanyProfileListCreateView.as_view(),name="all-profiles"),
    #retrieves profile details of the currently logged in Company party
    path("company-profile/<int:pk>",companyProfileDetailView.as_view(),name="profile"),
]