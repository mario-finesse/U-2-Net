import os
import shutil
from PIL import Image

def convert_png_to_jpg(png_path:str, jpg_path:str):
    image = Image.open(png_path)
    if image.mode == 'RGBA':
        background = Image.new('RGB', image.size, (255, 255, 255))
        background.paste(image, mask=image.split()[3])  # 3 is the alpha channel
        image = background
    image.save(jpg_path, 'JPEG')

images_path = "/data/clogen/ed_datasets/finesse_prods"
output_folder_path = "data/input/finesse_model_images"
for image_name in os.listdir(images_path):
    if "finesse" in image_name and image_name.endswith(".png"):
        source_file_path = os.path.join(images_path, image_name)
        print(f"Copying image {source_file_path}")
        destination_file_path = os.path.join(output_folder_path, image_name)
        destination_file_path = destination_file_path.replace(".png", ".jpg")
        convert_png_to_jpg(source_file_path, destination_file_path)
