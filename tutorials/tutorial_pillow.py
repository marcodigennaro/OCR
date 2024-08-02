from pathlib import Path
from PIL import Image
from ocr.config import PNG_DIR

image_file = Path(PNG_DIR).joinpath('offre.png')
image = Image.open(image_file)

print(image.size)
image.show()

