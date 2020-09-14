from rest_framework.views import APIView
from .asset_engine import AssetEngine
from accounts.models import PhaseDB
from django.http import HttpResponse


class FetchAsset(APIView):

    def get(self, request):
        advertiser_val = request.POST.get("Advertiser")
        user_val = request.POST.get("user_email")
        file_dest = request.POST.get("file_path")
        fetch_asset_object = AssetEngine()
        phase_data = PhaseDB.objects.filter(phase_user_email=user_val, phase_advertiser_name=advertiser_val)
        phase_position_list = [str(phase_data.phase_position) for phase_data in phase_data]
        print(phase_position_list)

        if phase_position_list == []:
            response = fetch_asset_object.asset_process_1(advertiser_val, user_val, file_dest)
            print("Phase 1 returned")
            return response

        elif phase_position_list[0] == "Phase-1":
            response = fetch_asset_object.asset_process_2(advertiser_val, user_val, file_dest)
            print("Phase 2 returned")
            return response

        elif phase_position_list[0] == "Phase-2":
            response = fetch_asset_object.asset_process_3(advertiser_val, user_val, file_dest)
            print("Phase 3 returned")
            return response

        elif phase_position_list[0] == "Phase-3":
            response = HttpResponse("All phase assets have been retrieved...")
            return response

        else:
            return HttpResponse("Error in retrieving phase...")


