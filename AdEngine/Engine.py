from django.template import loader
from AdRecords.models import Image
from distutils.dir_util import copy_tree
from accounts.models import AdvertiserProfile


class Engine:
    def logo_engine(self, request, image_property_id):
        global advertiser, logo_description
        image_path_list = []
        image_description_list = []
        ad_info = AdvertiserProfile.objects.all()
        image_id_info = Image.objects.filter(image_property_id=image_property_id)
        for i in image_id_info:
            image_path_list.append(i.image.path)
            image_description_list.append(i.image_description)
        for desc_val in image_description_list:
            logo_description = desc_val
        for ad_name in ad_info:
            advertiser = ad_name.advertiser_name
        for path in image_path_list:
            image_location = path
            template = loader.get_template('AdTemplates/demo/demo.html')
            context = {
                'image_location': image_location,
                'Advertiser': advertiser,
                'logo_description': logo_description,
            }
            phase_one_ad = template.render(context, request)
            src = 'AdRecords/templates/AdTemplates/demo'
            dest = 'AdAssets/{0}/Phase1'.format(advertiser)
            copy_tree(src, dest)
            with open('{0}/demo.html'.format(dest), 'w') as f:
                f.write(phase_one_ad)

        return True
