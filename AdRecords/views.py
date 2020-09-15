from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageSerializer, TextSerializer
from .models import Image, Text
from django.http import JsonResponse
from .helpers import MultipleFiles
from AdEngine.Engine import Engine
from NeuralNetEngine.generate import TextGen
from logger_settings import api_logger

class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        try:
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
                    phase_status = Engine()
                    phase_one_engine_status = phase_status.phase_one_engine(request, image_property_id)
                    if phase_one_engine_status:
                        api_logger.info("Phase one engine successfully executed...")
                        api_logger.info("Phase two engine to begin...")
                    phase_two_engine_status = phase_status.phase_two_engine(request, image_property_id)
                    if phase_two_engine_status:
                        api_logger.info("Phase two engine successfully executed...")
                        api_logger.info("Upload text for execution of Phase 3...")
                else:
                    flag = 0
            if flag == 1:
                api_logger.info("Image has been created..."+str(status))
                return Response(arr, status=status.HTTP_201_CREATED)

            else:
                api_logger.error("Image has not been created..." + str(status))
                return Response(arr, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            api_logger.exception("Exception in image upload..."+str(e))

    def get(self, request):
        try:
            all_images = Image.objects.all()
            serializer = ImageSerializer(all_images, many=True)
            api_logger.info("Retrieve image info..."+str(JsonResponse(serializer.data)))
            return JsonResponse(serializer.data, safe=False)

        except Exception as e:
            api_logger.exception("Unable to retrieve image..."+str(e))

class TextView(APIView):

    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        try:
            text_property_id = request.data['text_property_id']
            texts = request.data['text']
            flag = 1
            arr = []

            modified_data = MultipleFiles.modify_text(text_property_id, texts)
            text_serializer = TextSerializer(data=modified_data)
            if text_serializer.is_valid():
                text_serializer.save()
                arr.append(text_serializer.data)
                phase_three_status = Engine()
                phase_three_engine_status = phase_three_status.phase_three_engine(request, text_property_id)
                if phase_three_engine_status:
                    api_logger.info("Phase three has been successfully executed...")
            else:
                flag = 0
            if flag == 1:
                api_logger.info("Text has been created..."+str(status))
                return Response(arr, status=status.HTTP_201_CREATED)
            else:
                api_logger.error("Text has not been created..." + str(status))
                return Response(arr, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            api_logger.exception("Exception with text upload..."+str(e))

    def get(self, request):
        try:
            all_texts = Text.objects.all()
            serializer = TextSerializer(all_texts, many=True)
            api_logger.info("Text has not been created..." + str(status))
            return JsonResponse(serializer.data, safe=False)

        except Exception as e:
            api_logger.error("Unable to retrieve text..." + str(e))


