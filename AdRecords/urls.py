from django.conf.urls import url
from .views import ImageView, TextView

urlpatterns = [
  	url(r'^upload-image/$', ImageView.as_view(), name='file-upload'),
	url(r'^upload-text/$', TextView.as_view(), name='text-upload'),
]