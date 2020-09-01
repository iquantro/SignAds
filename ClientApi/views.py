from rest_framework.views import APIView
from .asset_engine import AssetEngine


class FetchAsset(APIView):

    def get(self, request):
        fetch_asset_object = AssetEngine()
        response = fetch_asset_object.asset_process(request)
        return response
