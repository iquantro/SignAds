from django.http import HttpResponse
from shutil import make_archive
from wsgiref.util import FileWrapper
from os import path

class PhaseOne:

    def get(self, advertiser_val):
        adpath = "/home/nithin/Startup/SignAds/AdAssets/{0}/Phase1".format(advertiser_val) #make sure to change path
        file_name = "{0}".format(advertiser_val)
        if path.exists(adpath):
            path_to_zip = make_archive("Downloads", "zip", adpath)
            response = HttpResponse(FileWrapper(open(path_to_zip, 'rb')), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename="{filename}.zip"'.format(filename=file_name)
            return response
        else:
            print("File path does not exist...")
            response = HttpResponse("File path does not exist...")
            return response


class PhaseTwo:#test api for phase2 video servicing

    def get(self, advertiser_val):
        adpath = "/home/nithin/Startup/SignAds/AdAssets/{0}/Phase2/".format(advertiser_val)
        file_name = "{0}.mp4".format(advertiser_val)
        video_path = adpath+file_name
        if path.exists(video_path):
            file = FileWrapper(open(video_path, 'rb'))
            response = HttpResponse(file, content_type='video/mp4')
            response['Content-Disposition'] = 'attachment; filename="{filename}.zip"'.format(filename=file_name)
            return response
        else:
            print("File path error...")
            response = HttpResponse("File path does not exist...")
            return response

class PhaseThree:

    def get(self, advertiser_val):
        adpath = "/home/nithin/Startup/SignAds/AdAssets/{0}/Phase3".format(advertiser_val) #make sure to change path
        file_name = "{0}".format(advertiser_val)
        if path.exists(adpath):
            path_to_zip = make_archive("Downloads", "zip", adpath)
            response = HttpResponse(FileWrapper(open(path_to_zip, 'rb')), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename="{filename}.zip"'.format(filename=file_name)
            return response
        else:
            print("File path error...")
            response = HttpResponse("File path does not exist...")
            return response


