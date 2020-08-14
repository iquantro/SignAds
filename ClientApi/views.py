from rest_framework.views import APIView
from django.shortcuts import render


class AdService(APIView):

    def get(self, request):
        Advertiser = request.POST.get('Advertiser')
        Adpath = "{0}/Phase1/demo.html".format(Advertiser)
        return render(request, Adpath)
