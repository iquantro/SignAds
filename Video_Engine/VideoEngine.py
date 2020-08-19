import os
from PIL import Image
from PIL import ImageDraw, ImageFont
from AdRecords.models import Image as dbImg
import json

class VideoEngine:
    global img_name
    global image_val, image_id_info
    image_path_list = []
    image_description_list = []

    def converter(self, image_property_id, advertiser, advertiser_desc):

        capture_time = 15
        video_fps = 20
        image_engine_path_json = '/home/nithin/Startup/SignAds/Video_Engine/paths.json'
        with open(image_engine_path_json, "r") as rf:
            paths = json.load(rf)

        image_id_info = dbImg.objects.filter(image_property_id=image_property_id)
        img_name = [str(image_val.image) for image_val in image_id_info][0]

        media_path_in = paths['paths']['media_dir_path']
        media_path_out = paths['paths']['media_path_out']

        img1 = Image.open('Video_Engine/background.jpg')
        img2 = Image.open(media_path_in+img_name)
        BackImg = img1.copy()
        BackImg.paste(img2)

        font = ImageFont.truetype('Fonts/Roboto-Black.ttf', size=200)

        (x,y) = (500, 500)
        message = advertiser
        color = 'rgb(0, 0, 0)' # color specification
        draw = ImageDraw.Draw(BackImg)
        draw.text((x, y), message, fill=color, font=font)

        font = ImageFont.truetype('Fonts/Roboto-Black.ttf', size=50)
        (x, y) = (700,700)
        name = advertiser_desc
        color = 'rgb(0, 128, 255)' # white color
        draw.text((x, y), name, fill=color, font=font)

        BackImg.save('/home/nithin/Startup/SignAds/Video_Engine/'+advertiser+'.jpg', quality=95)
        print("image created")

        video_engine_path = paths['paths']['VideoEngine_path']
        save_dir = os.path.join(media_path_out+advertiser,"phase2")
        os.mkdir(save_dir)
        #cmd = "ffmpeg -i video.mp4 -i hypnosis.wav -c:v copy -c:a aac output.mp4"
        cmd = "ffmpeg -loop 1 -i {0} -i ".format(video_engine_path+advertiser+'.jpg')+video_engine_path+"hypnosis.wav -c:v libx264 -t 15 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {0}/{1}.mp4".format(save_dir, advertiser)
        os.system(cmd)
        os.remove(video_engine_path+advertiser+".jpg")

