
class MultipleFiles:
    def modify_text(text_property_id, text):
        dict = {}
        dict['text_property_id'] = text_property_id
        dict['text'] = text
        return dict

    def modify_image(image_property_id, image):
        dict = {}
        dict['image_property_id'] = image_property_id
        dict['image'] = image
        return dict
