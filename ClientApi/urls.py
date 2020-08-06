from django.conf.urls import url
from .views import AdService

urlpatterns = [
    url(r'^Adservice', AdService.as_view(), name='ClientApi'),
]