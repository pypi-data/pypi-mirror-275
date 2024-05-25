# image_helpers/image_ops.py

from PIL import Image, ImageFilter

def resize_image(input_path, output_path, size):
    """画像をリサイズします"""
    with Image.open(input_path) as img:
        img = img.resize(size)
        img.save(output_path)

def convert_image_format(input_path, output_path, format):
    """画像のフォーマットを変換します"""
    with Image.open(input_path) as img:
        img.save(output_path, format=format)

def apply_blur_filter(input_path, output_path, radius=2):
    """画像にぼかしフィルターを適用します"""
    with Image.open(input_path) as img:
        img = img.filter(ImageFilter.GaussianBlur(radius))
        img.save(output_path)

def apply_sharp_filter(input_path, output_path):
    """画像にシャープフィルターを適用します"""
    with Image.open(input_path) as img:
        img = img.filter(ImageFilter.SHARPEN)
        img.save(output_path)
