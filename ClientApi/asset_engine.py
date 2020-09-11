from .get_assets import PhaseOne, PhaseTwo, PhaseThree
from .save_phase import Phasesave
from accounts.models import PhaseDB
from django.http import HttpResponse

class AssetEngine:
    def asset_process_1(self, advertiser_val, user_val, file_dest):

        #Phase one asset fetching
        phase_one_object = PhaseOne()
        asset_response = phase_one_object.get(advertiser_val, file_dest)

        phase_val = "Phase-1"
        phase_save_object = Phasesave()
        phase_save_object.phase_save(phase_val, user_val, advertiser_val)

        return asset_response

    def asset_process_2(self, advertiser_val, user_val, file_dest):

        #Phase two asset fetching
        phase_two_object = PhaseTwo()
        asset_response = phase_two_object.get(advertiser_val, file_dest)
        phase_save_object = Phasesave()
        phase_save_object.phase_save("Phase-2", user_val, advertiser_val)

        return asset_response


    def asset_process_3(self, advertiser_val, user_val, file_dest):

        #Phase three asset fetching
        phase_three_object = PhaseThree()
        asset_response = phase_three_object.get(advertiser_val, file_dest)
        phase_save_object = Phasesave()
        phase_save_object.phase_save("Phase-3", user_val, advertiser_val)

        #When all three phases are fetched by client
        phase_val = "All phases completed..."
        complete_phase_save_object = Phasesave()
        complete_phase_save_object.phase_save(phase_val, user_val, advertiser_val)

        return asset_response





