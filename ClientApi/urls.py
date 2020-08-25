from django.conf.urls import url
from .views import AdService, PhaseTwo, PhaseThree

urlpatterns = [
    url(r'^Adservice', AdService.as_view(), name='ClientApi'),
    url(r'^PhaseTwo', PhaseTwo.as_view(), name='PhaseTwo'),
    url(r'^PhaseThree', PhaseThree.as_view(), name='PhaseThree'),
]