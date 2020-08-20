from django.template import loader
from AdRecords.models import Image
from accounts.models import AdvertiserProfile
from distutils.dir_util import copy_tree
import shutil
import json
from Video_Engine.VideoEngine import VideoEngine

class Engine:
    def phase_one_engine(self, request, image_property_id):
        global image_engine_path_json
        image_engine_path_json = "E:/SignAds/AdEngine/paths.json"
        global advertiser, logo_description, advertiser_desc
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
            advertiser_desc = ad_name.advertiser_description

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

        return True

    def phase_two_engine(self, request, image_property_id):
        ad_info = AdvertiserProfile.objects.all()
        advertiser_desc_val = [str(ad_name.advertiser_description) for ad_name in ad_info][0]
        advertiser_val = [str(ad_name.advertiser_name) for ad_name in ad_info][0]
        video_engine_object = VideoEngine()
        video_engine_object.converter(image_property_id, advertiser_val, advertiser_desc_val)

        return True


