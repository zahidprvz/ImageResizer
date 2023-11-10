# image_resizer.py
from PIL import Image
import os

def resize_image(image_path, width, height):
    output_path = f"static/resized_images/{os.path.basename(image_path)}"
    with Image.open(image_path) as img:
        img.thumbnail((width, height))
        img.save(output_path)
