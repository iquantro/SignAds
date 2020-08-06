from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.template import loader

class AdService(APIView):

    def get(self, request):
        Advertiser = request.POST.get('Advertiser')
        Adpath = "{0}/Phase1/demo.html".format(Advertiser)
        #Ad = loader.get_template(Adpath)
        return render(request,Adpath)



