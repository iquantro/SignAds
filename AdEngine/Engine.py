from django.template import loader
from AdRecords.models import Image
from accounts.models import AdvertiserProfile
from distutils.dir_util import copy_tree
import shutil, os


class Engine:
    def logo_engine(self, request, image_property_id):
        global advertiser, logo_description
        global dest, img_name
        dest = 'E:/SignAds/AdRecords/templates/AdTemplates/demo/assets/'
        media_path = 'E:/SignAds/media/'
        asset_str = 'assets/'
        image_path_list = []
        image_description_list = []
        ad_info = AdvertiserProfile.objects.all()
        image_id_info = Image.objects.filter(image_property_id=image_property_id)
        for i in image_id_info:
            image_path_list.append(i.image.path)
            image_description_list.append(i.image_description)
            img_name = str(i.image)
        for desc_val in image_description_list:
            logo_description = desc_val
        for ad_name in ad_info:
            advertiser = ad_name.advertiser_name

        shutil.copy(media_path+img_name, dest)
        image_location = asset_str+img_name
        template = loader.get_template('AdTemplates/demo/demo.html')
        context = {
                'image_location': image_location,
                'Advertiser': advertiser,
                'logo_description': logo_description,
        }
        phase_one_ad = template.render(context, request)
        src = 'AdRecords/templates/AdTemplates/demo'
        ad_dest = 'AdAssets/{0}/Phase1'.format(advertiser)
        copy_tree(src, ad_dest)
        with open('{0}/demo.html'.format(ad_dest), 'w') as f:
            f.write(phase_one_ad)

        os.remove(src+'/'+asset_str+img_name)

        return True
