from django.conf.urls import url
from .views import FetchAsset

urlpatterns = [
    url(r'^FetchAsset', FetchAsset.as_view(), name='FetchAsset'),
]