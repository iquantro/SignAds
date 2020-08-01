from django.conf.urls import url
from .views import AdvertiserView, UserView

urlpatterns = [
    url(r'^user-profile', UserView.as_view(), name='profile'),
    url(r'^advertiser-profile', AdvertiserView.as_view(), name='profile'),
]