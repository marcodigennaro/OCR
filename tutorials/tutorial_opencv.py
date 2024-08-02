from pathlib import Path
from ocr.config import PNG_DIR

import cv2

image_file = Path(PNG_DIR).joinpath('offre.png')
img = cv2.imread(image_file)


