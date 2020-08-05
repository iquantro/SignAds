from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageSerializer, TextSerializer
from .models import Image, Text
from django.http import JsonResponse
from .helpers import MultipleFiles
from AdEngine.Engine import Engine

class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        image_property_id = request.data['image_property_id']
        images = dict((request.data).lists())['image']
        flag = 1
        arr = []
        for img_name in images:
            modified_data = MultipleFiles.modify_image(image_property_id, img_name)
            image_serializer = ImageSerializer(data=modified_data)
            if image_serializer.is_valid():
                image_serializer.save()
                arr.append(image_serializer.data)
                phase_one_status = Engine()
                phase_one_engine_status = phase_one_status.phase_one_engine(request, image_property_id)
                if phase_one_engine_status:
                    print("Logo engine successfully executed...")
            else:
                flag = 0
        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
            return Response(arr, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        all_images = Image.objects.all()
        serializer = ImageSerializer(all_images, many=True)
        return JsonResponse(serializer.data, safe=False)

class TextView(APIView):

    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        text_property_id = request.data['text_property_id']
        texts = request.data['text']
        flag = 1
        arr = []

        modified_data = MultipleFiles.modify_text(text_property_id, texts)
        text_serializer = TextSerializer(data=modified_data)
        if text_serializer.is_valid():
            text_serializer.save()
            arr.append(text_serializer.data)
        else:
            flag = 0
        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
            return Response(arr, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        all_texts = Text.objects.all()
        serializer = TextSerializer(all_texts, many=True)
        return JsonResponse(serializer.data, safe=False)


