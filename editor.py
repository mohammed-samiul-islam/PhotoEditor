from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'
output_path = './edited'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    clean_name = os.path.splitext(filename)[0]
    edit.save(f"{output_path}/{clean_name}_edited.jpg")