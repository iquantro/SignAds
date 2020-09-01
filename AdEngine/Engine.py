from AdRecords.models import Text
from accounts.models import AdvertiserProfile, PhaseDB, userProfile
from Video_Engine.VideoEngine import VideoEngine
from NeuralNetEngine.generate import TextGen
from BlippingEngine.phase_one import BlippingEngine

class Engine:
    def phase_one_engine(self, request, image_property_id):
        phase_one_engine_object = BlippingEngine()
        phase_one_engine_object.blip_generator(request, image_property_id)
        #phase one tracker
        user_info = userProfile.objects.all()
        advertiser_info = AdvertiserProfile.objects.all()
        phase1_advertiser = [str(phase1_ad.advertiser_name) for phase1_ad in advertiser_info][0]
        phase1_user = [str(phase1_user.user_email) for phase1_user in user_info][0]
        phase1_val = "Phase-1"
        phase_data = PhaseDB(phase_position=phase1_val, phase_user_email=phase1_user,
                             phase_advertiser_name=phase1_advertiser)
        phase_data.save()
        return True

    def phase_two_engine(self, request, image_property_id):
        ad_info = AdvertiserProfile.objects.all()
        advertiser_desc_val = [str(ad_name.advertiser_description) for ad_name in ad_info][0]
        advertiser_val = [str(ad_name.advertiser_name) for ad_name in ad_info][0]
        video_engine_object = VideoEngine()
        video_engine_object.converter(image_property_id, advertiser_val, advertiser_desc_val)

        #phase two tracker
        user_info = userProfile.objects.all()
        advertiser_info = AdvertiserProfile.objects.all()
        phase2_advertiser = [str(phase2_ad.advertiser_name) for phase2_ad in advertiser_info][0]
        phase2_user = [str(phase2_user.user_email) for phase2_user in user_info][0]
        phase2_val = "Phase-2"
        phase_data = PhaseDB(phase_position=phase2_val, phase_user_email=phase2_user,
                             phase_advertiser_name=phase2_advertiser)
        phase_data.save()
        return True

    def phase_three_engine(self, request, text_property_id):
        text_id_info = Text.objects.filter(text_property_id=text_property_id)
        text_val = [str(text_value.text) for text_value in text_id_info][0]
        # emotional text generation engine
        text_gen_object = TextGen()
        text_gen_object.textgenerator(request, text_val, text_property_id)
        #phase three tracker
        user_info = userProfile.objects.all()
        advertiser_info = AdvertiserProfile.objects.all()
        phase3_advertiser = [str(phase3_ad.advertiser_name) for phase3_ad in advertiser_info][0]
        phase3_user = [str(phase3_user.user_email) for phase3_user in user_info][0]
        phase3_val = "Phase-3"
        phase_data = PhaseDB(phase_position=phase3_val, phase_user_email=phase3_user,
                             phase_advertiser_name=phase3_advertiser)
        phase_data.save()
        return True
