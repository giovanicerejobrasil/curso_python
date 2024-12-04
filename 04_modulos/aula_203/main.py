"""
Pillow: redimensionando imagens com Python
Essa biblioteca é o 'Photoshop' do Python 😋
"""
from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL_IMAGE = ROOT_FOLDER / 'original_image.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new_image.jpg'

pil_image = Image.open(ORIGINAL_IMAGE)
height, width = pil_image.size
# exif = pil_image.info['exif']

"""
width   new_width
height  X

OR

height  new_height
width   X
"""
new_height = 1080
new_width = round(width * new_height / height)

new_image = pil_image.resize(size=(new_height, new_width))
new_image_with_rotate = new_image.rotate(90, expand=1)

new_image_with_rotate.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    # exif=exif
)
