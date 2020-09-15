from .get_assets import PhaseOne, PhaseTwo, PhaseThree
from .save_phase import Phasesave
from accounts.models import PhaseDB
from django.http import HttpResponse
from logger_settings import api_logger

class AssetEngine:
    def asset_process_1(self, advertiser_val, user_val, file_dest):
        try:
            #Phase one asset fetching
            api_logger.info("Phase one asset process has started...")
            api_logger.info("Phase one asset fetch has started...")
            phase_one_object = PhaseOne()
            asset_response = phase_one_object.get(advertiser_val, file_dest)
            api_logger.info("Phase one asset has been fetched...")
            api_logger.info("Phase state saving for Phase one started...")
            phase_val = "Phase-1"
            phase_save_object = Phasesave()
            phase_save_object.phase_save(phase_val, user_val, advertiser_val)
            api_logger.info("Phase state has been saved for Phase one...")
            return asset_response

        except Exception as e:
            api_logger.info("Exception in Phase-1 asset process..."+str(e))

    def asset_process_2(self, advertiser_val, user_val, file_dest):
        try:
            #Phase two asset fetching
            api_logger.info("Phase two asset process has started...")
            api_logger.info("Phase two asset fetching has started")
            phase_two_object = PhaseTwo()
            asset_response = phase_two_object.get(advertiser_val, file_dest)
            api_logger.info("Phase two asset has been fetched...")
            api_logger.info("Phase state saving for phase two started...")
            phase_save_object = Phasesave()
            phase_save_object.phase_save("Phase-2", user_val, advertiser_val)
            api_logger.info("Phase two state has been saved...")
            return asset_response

        except Exception as e:
            api_logger.exception("Exception in Phase-2 asset process..."+str(e))


    def asset_process_3(self, advertiser_val, user_val, file_dest):
        try:
            #Phase three asset fetching
            api_logger.info("Phase three asset process has started...")
            api_logger.info("Phase three asset fetching has started...")
            phase_three_object = PhaseThree()
            api_logger.info("Phase three asset fetching has started...")
            asset_response = phase_three_object.get(advertiser_val, file_dest)
            api_logger.info("Phase three asset has been fetched...")
            api_logger.info("Phase three saving has started...")
            phase_save_object = Phasesave()
            phase_save_object.phase_save("Phase-3", user_val, advertiser_val)
            api_logger.info("Phase three state has been saved...")
            #When all three phases are fetched by client
            api_logger.info("All phases have been completed...")
            phase_val = "All phases completed..."
            complete_phase_save_object = Phasesave()
            complete_phase_save_object.phase_save(phase_val, user_val, advertiser_val)
            return asset_response

        except Exception as e:
            api_logger.exception("Exception in Phase-3 asset process..."+str(e))





