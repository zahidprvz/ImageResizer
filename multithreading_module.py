# multithreading_module.py
from concurrent.futures import ThreadPoolExecutor
from image_resizer import resize_image
import os

def resize_images_parallel(image_paths, width, height):
    with ThreadPoolExecutor() as executor:
        executor.map(lambda path: resize_image(path, width, height), image_paths)
