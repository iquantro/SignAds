from django.template import loader
from AdRecords.models import Image
from accounts.models import AdvertiserProfile
from distutils.dir_util import copy_tree
import shutil
import json
import os
import cv2
from os.path import isfile, join
import moviepy.editor as mpe
import ffmpeg
import subprocess
import time


class Engine:
    def phase_one_engine(self, request, image_property_id):
        global image_engine_path_json
        image_engine_path_json = "E:/SignAds/AdEngine/paths.json"
        global advertiser, logo_description
        global dest, img_name
        with open(image_engine_path_json, "r") as rf:
            paths = json.load(rf)
        dest = paths['paths']['asset_destination_path']
        media_path = paths['paths']['media_dir_path']
        asset_str = paths['paths']['relative_assets_dir_path']
        image_path_list = []
        image_description_list = []
        ad_info = AdvertiserProfile.objects.all()
        image_id_info = Image.objects.filter(image_property_id=image_property_id)
        for image_val in image_id_info:
            image_path_list.append(image_val.image.path)
            image_description_list.append(image_val.image_description)
            img_name = str(image_val.image)
        for desc_val in image_description_list:
            logo_description = desc_val
        for ad_name in ad_info:
            advertiser = ad_name.advertiser_name

        shutil.copy(media_path + img_name, dest)
        image_location = asset_str + img_name
        template = loader.get_template(paths['paths']['relative_template_html_file_path'])
        context = {
            'image_location': image_location,
            'Advertiser': advertiser,
            'logo_description': logo_description,
        }
        phase_one_ad = template.render(context, request)
        src = paths['paths']['relative_template_dir_path']
        ad_dest = 'AdAssets/{0}/Phase1'.format(advertiser)
        copy_tree(src, ad_dest)
        with open('{0}/demo.html'.format(ad_dest), 'w') as f:
            f.write(phase_one_ad)

        os.remove(src + '/' + asset_str + img_name)

        return True

    def phase_two_engine(self, request, image_property_id):

        image_path_list = []
        image_description_list = []
        capture_time = 15
        video_fps = 20.0
        with open(image_engine_path_json, "r") as rf:
            paths = json.load(rf)

        media_path_in = paths['paths']['media_dir_path']
        media_path_out = paths['paths']['media_path_out']
        image_id_info = Image.objects.filter(image_property_id=image_property_id)
        for image_val in image_id_info:
            image_path_list.append(image_val.image.path)
            image_description_list.append(image_val.image_description)
            img_name = str(image_val.image)
        frame_array = []
        files = [f for f in os.listdir(media_path_in) if isfile(join(media_path_in, f))]
        # for sorting the file names properly
        files.sort(key=lambda x: x[5:-4])
        files.sort()
        frame_array = []
        files = [f for f in os.listdir(media_path_in) if isfile(join(media_path_in, f))]
        # for sorting the file names properly
        files.sort(key=lambda x: x[5:-4])
        for i in range(len(files)):
            filename = media_path_in+img_name
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width, height)
            frame_array.append(img)
        out = cv2.VideoWriter(media_path_out, cv2.VideoWriter_fourcc(*'DIVX'), video_fps, size)
        start_time = time.time()
        while int(time.time() - start_time) < capture_time:
            for i in range(len(frame_array)):
                out.write(frame_array[i])
        out.release()
        '''
        videofile = paths["paths"]["video_abs_path"].split("/")[2]
        audiofile = paths["paths"]["mp3_abs_path"].split("/")[3]
        video_stream = ffmpeg.input(videofile)
        audio_stream = ffmpeg.input(audiofile)
        ffmpeg.output(audio_stream, video_stream, 'out.avi').run()
        '''
        return True


