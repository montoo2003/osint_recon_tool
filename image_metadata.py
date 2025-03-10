from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()

    if not exif_data:
        return "No metadata found."
    
    metadata = {TAGS.get(tag): value for tag, value in exif_data.items()}
    return metadata
