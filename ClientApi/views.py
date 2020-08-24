from rest_framework.views import APIView
from django.http import HttpResponse
from shutil import make_archive
from wsgiref.util import FileWrapper


class AdService(APIView):

    def get(self, request):
        advertiser = request.POST.get('Advertiser')
        adpath = "E:/SignAds/AdAssets/{0}/Phase1".format(advertiser) #make sure to change path
        file_name = "{0}".format(advertiser)
        path_to_zip = make_archive("Downloads", "zip", adpath)
        response = HttpResponse(FileWrapper(open(path_to_zip, 'rb')), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="{filename}.zip"'.format(filename=file_name)
        return response
