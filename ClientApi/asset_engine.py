from .get_assets import PhaseOne, PhaseTwo, PhaseThree
from .save_phase import Phasesave
from accounts.models import PhaseDB
from django.http import HttpResponse

class AssetEngine:
    def asset_process(self, request):
        advertiser_val = request.POST.get("Advertiser")
        user_val = request.POST.get("user_email")
        file_dest = request.POST.get("file_path")

        #Phase one asset fetching
        phase_one_object = PhaseOne()
        phase_one_object.get(advertiser_val, file_dest)

        phase_val = "Phase-1"
        phase_save_object = Phasesave()
        phase_save_object.phase_save(phase_val, user_val, advertiser_val)
        phase_data = PhaseDB.objects.filter(phase_user_email=user_val, phase_advertiser_name=advertiser_val)
        phase_position_str = [str(phase_data.phase_position) for phase_data in phase_data][0]
        #Phase two asset fetching
        if phase_position_str == "Phase-1":
            phase_two_object = PhaseTwo()
            phase_two_object.get(advertiser_val, file_dest)
            phase_save_object = Phasesave()
            phase_save_object.phase_save("Phase-2", user_val, advertiser_val)
        else:
            return HttpResponse("Phase one asset not yet retrieved...")
        #Phase three asset fetching
        if phase_position_str == "Phase-2":
            phase_three_object = PhaseThree()
            phase_three_object.get(advertiser_val, file_dest)
            phase_save_object = Phasesave()
            phase_save_object.phase_save("Phase-3", user_val, advertiser_val)
        else:
            return HttpResponse("Phase two asset not yet retrieved but Phase one retrieved...")
        #When all three phases are fetched by client
        if phase_position_str == "Phase-3":
            phase_val = "All phases completed..."
            phase_save_object = Phasesave()
            phase_save_object.phase_save(phase_val, user_val, advertiser_val)
        else:
            return HttpResponse("Phase three asset not yet executed but phase one and phase two executed...")



