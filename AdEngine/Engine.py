from AdRecords.models import Text
from accounts.models import AdvertiserProfile, PhaseDB, userProfile
from Video_Engine.VideoEngine import VideoEngine
from NeuralNetEngine.generate import TextGen
from BlippingEngine.phase_one import BlippingEngine

class Engine:
    def phase_one_engine(self, request, image_property_id):
        phase_one_engine_object = BlippingEngine()
        phase_one_engine_object.blip_generator(request, image_property_id)
        return True

    def phase_two_engine(self, request, image_property_id):
        ad_info = AdvertiserProfile.objects.all()
        advertiser_desc_val = [str(ad_name.advertiser_description) for ad_name in ad_info][0]
        advertiser_val = [str(ad_name.advertiser_name) for ad_name in ad_info][0]
        video_engine_object = VideoEngine()
        video_engine_object.converter(image_property_id, advertiser_val, advertiser_desc_val)
        return True

    def phase_three_engine(self, request, text_property_id):
        text_id_info = Text.objects.filter(text_property_id=text_property_id)
        text_val = [str(text_value.text) for text_value in text_id_info][0]
        # emotional text generation engine
        text_gen_object = TextGen()
        text_gen_object.textgenerator(request, text_val, text_property_id)
        return True
