import os
from PIL import Image
from PIL import ImageDraw, ImageFont
from AdRecords.models import Image as dbImg
import json
import os
from logger_settings import api_logger

class VideoEngine:
    global img_name
    global image_val, image_id_info
    image_path_list = []
    image_description_list = []

    def converter(self, image_property_id, advertiser, advertiser_desc):
        try:
            capture_time = 15
            video_fps = 20
            file = os.getcwd()
            base_path = file
            image_engine_path_json = "/"+base_path+'/Video_Engine/paths.json'
            with open(image_engine_path_json, "r") as rf:
                paths = json.load(rf)

            image_id_info = dbImg.objects.filter(image_property_id=image_property_id)
            img_name = [str(image_val.image) for image_val in image_id_info][0]

            media_path_in = "/"+base_path+paths['paths']['media_dir_path']
            media_path_out = "/"+base_path+paths['paths']['media_path_out']

            img1 = Image.open('Video_Engine/background.jpg')
            img2 = Image.open(media_path_in + img_name)
            BackImg = img1.copy()
            BackImg.paste(img2)

            font = ImageFont.truetype('Fonts/Roboto-Black.ttf', size=200)

            (x, y) = (500, 500)
            message = advertiser
            color = 'rgb(0, 0, 0)'  # color specification
            draw = ImageDraw.Draw(BackImg)
            draw.text((x, y), message, fill=color, font=font)

            font = ImageFont.truetype('Fonts/Roboto-Black.ttf', size=50)
            (x, y) = (700, 700)
            name = advertiser_desc
            color = 'rgb(0, 128, 255)'  # white color
            draw.text((x, y), name, fill=color, font=font)

            video_engine_path = "/"+base_path+paths['paths']['VideoEngine_path']
            BackImg.save(video_engine_path + advertiser + '.jpg', quality=95)
            api_logger.info("Image has been created...")

            save_dir = os.path.join(media_path_out + advertiser, "Phase2")
            os.mkdir(save_dir)
            api_logger.info("Video conversion has started..."+str(save_dir))
            cmd = "ffmpeg -loop 1 -i {0} -i ".format(
                video_engine_path + advertiser + '.jpg') + video_engine_path + "hypnosis.wav -c:v libx264 -t 15 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {0}/{1}.mp4".format(
                save_dir, advertiser)
            api_logger.info("Video conversion has finished..." + str(save_dir))
            os.system(cmd)
            os.remove(video_engine_path + advertiser + ".jpg")

        except Exception as e:
            api_logger.exception("Exception has occurred in video engine..."+str(e))