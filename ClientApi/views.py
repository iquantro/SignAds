from rest_framework.views import APIView
from .asset_engine import AssetEngine
from accounts.models import PhaseDB
from django.http import HttpResponse
from logger_settings import api_logger

class FetchAsset(APIView):

    def get(self, request):
        try:
            advertiser_val = request.POST.get("Advertiser")
            user_val = request.POST.get("user_email")
            file_dest = request.POST.get("file_path")
            fetch_asset_object = AssetEngine()
            phase_data = PhaseDB.objects.filter(phase_user_email=user_val, phase_advertiser_name=advertiser_val)
            phase_position_list = [str(phase_data.phase_position) for phase_data in phase_data]
            api_logger.info("List of phase position..."+str(phase_position_list))

            if phase_position_list == []:
                response = fetch_asset_object.asset_process_1(advertiser_val, user_val, file_dest)
                api_logger.info("Phase one asset has been returned")
                return response

            elif phase_position_list[0] == "Phase-1":
                response = fetch_asset_object.asset_process_2(advertiser_val, user_val, file_dest)
                api_logger.info("Phase one asset has been returned")
                return response

            elif phase_position_list[0] == "Phase-2":
                response = fetch_asset_object.asset_process_3(advertiser_val, user_val, file_dest)
                api_logger.info("Phase two asset has been returned")
                return response

            elif phase_position_list[0] == "Phase-3":
                response = HttpResponse("All phase assets have been retrieved...")
                api_logger.info("Phase three has been retrieved...")
                return response

            else:
                api_logger.info("Error in retrieving phase...")
                return HttpResponse("Error in retrieving phase...")

        except Exception as e:
            api_logger.exception("Exception in FetchAsset view..."+str(e))

