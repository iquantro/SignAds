from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
import logging
from simpletransformers.language_generation import LanguageGenerationModel
import json
from django.template import loader
from AdRecords.models import Image
from accounts.models import AdvertiserProfile
from distutils.dir_util import copy_tree
import shutil
import os


class TextGen:
    def textgenerator(self, request, text_val, text_property_id):
        logging.basicConfig(level=logging.INFO)
        transformers_logger = logging.getLogger("transformers")
        transformers_logger.setLevel(logging.WARNING)
        model = LanguageGenerationModel("gpt2", "gpt2", args={"length": 256}, use_cuda=False)
        prompts = ["{0}".format(text_val)]
        # Generate text using the model. Verbose set to False to prevent logging generated sequences.
        generated = [str(prompt) for prompt in model.generate(prompts, verbose=False)][0]
        final_generated_txt = ['.'.join(generated[0].split('.')[:-1]) + '.'][0]
        file = os.path.join(os.getcwd(), os.listdir(os.getcwd())[0]).replace("\\", '/')
        base_path = file.strip("/.git")
        image_engine_path_json = base_path+"/AdEngine/paths.json"
        with open(image_engine_path_json, "r") as rf:
            paths = json.load(rf)
        dest = paths['paths']['asset_destination_path']
        media_path = paths['paths']['media_dir_path']
        asset_path_str = paths['paths']['relative_assets_dir_path']
        ad_info = AdvertiserProfile.objects.all()
        image_id_info = Image.objects.filter(image_property_id=text_property_id) #image and text property id should be the same
        img_name = [str(image_val.image) for image_val in image_id_info][0]
        advertiser = [str(ad_name.advertiser_name) for ad_name in ad_info][0]
        shutil.copy(media_path + img_name, dest)
        image_location = asset_path_str + img_name
        template = loader.get_template(paths['paths']['relative_template_html_file_path'])
        context = {
            'image_location': image_location,
            'Advertiser': advertiser,
            'logo_description': final_generated_txt,
        }
        phase_three_ad = template.render(context, request)
        src = paths['paths']['relative_template_dir_path']
        ad_dest = 'AdAssets/{0}/Phase3'.format(advertiser)
        copy_tree(src, ad_dest)
        with open('{0}/demo.html'.format(ad_dest), 'w') as f:
            f.write(phase_three_ad)
        print("Phase3 assets created for advertiser {0}".format(advertiser))
