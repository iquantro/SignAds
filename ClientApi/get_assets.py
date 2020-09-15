from django.http import HttpResponse
from shutil import make_archive
from wsgiref.util import FileWrapper
from os import path
from django.http import FileResponse
import os
from logger_settings import api_logger

class PhaseOne:

    def get(self, advertiser_val, file_dest):

        try:
            file = os.path.join(os.getcwd(), os.listdir(os.getcwd())[0]).replace("\\", '/')
            base_path = file.strip("/.git")
            adpath = "/"+base_path+"/AdAssets/{0}/Phase1".format(advertiser_val) #make sure to change path
            file_name = "{0}".format(advertiser_val)
            if path.exists(adpath):
                #place client destination directory in make_archive.
                path_to_zip = make_archive(file_name, "zip", adpath)
                file = FileWrapper(open(path_to_zip, 'rb'))
                response = HttpResponse(file, content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename="{0}.zip"'.format(file_name)
                api_logger.info("Phase one Asset has been returned...")
                return response
            else:
                api_logger.error("File path does not exist for Phase one asset...")
                response = HttpResponse("File path does not exist for Phase one asset...")
                return response

        except Exception as e:
            api_logger.exception("Exception in Phase one asset fetching...")


class PhaseTwo:#test api for phase2 video servicing

    def get(self, advertiser_val, file_dest):

        try:
            file = os.path.join(os.getcwd(), os.listdir(os.getcwd())[0]).replace("\\", '/')
            base_path = file.strip("/.git")
            adpath = "/"+base_path+"/AdAssets/{0}/Phase2/".format(advertiser_val)
            file_name = "{0}.mp4".format(advertiser_val)
            video_path = adpath+file_name
            api_logger.info("Video path..."+str(video_path))
            if path.exists(video_path):
                file = FileWrapper(open(video_path, 'rb'))
                response = HttpResponse(file, content_type='video/mp4')
                response['Content-Disposition'] = 'attachment; filename="{0}'.format(file_name)
                api_logger.info("Phase two Asset has been returned...")
                return response
            else:
                api_logger.info("File path does not exist for phase two asset...")
                response = HttpResponse("File path does not exist for phase two asset...")
                return response

        except Exception as e:
            api_logger.exception("Exception in Phase two asset fetching...")

class PhaseThree:

    def get(self, advertiser_val, file_dest):

        try:
            file = os.path.join(os.getcwd(), os.listdir(os.getcwd())[0]).replace("\\", '/')
            base_path = file.strip("/.git")
            adpath = "/"+base_path+"/AdAssets/{0}/Phase3".format(advertiser_val)  #make sure to change path
            file_name = "{0}".format(advertiser_val)
            if path.exists(adpath):
                path_to_zip = make_archive(file_name, "zip", adpath)
                file = FileWrapper(open(path_to_zip, 'rb'))
                response = HttpResponse(file, content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename="{0}.zip"'.format(file_name)
                api_logger.info("Phase three Asset has been returned...")
                return response
            else:
                print("File path error...")
                response = HttpResponse("File path does not exist...")
                api_logger.info("File path does not exist...")
                return response

        except Exception as e:
            api_logger.exception("Exception in retrieving Phase three asset..."+str(e))

