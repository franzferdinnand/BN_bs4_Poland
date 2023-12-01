import pytesseract
from PIL import Image, ImageFile


ImageFile.LOAD_TRUNCATED_IMAGES = True


def fetch_email_from_pic(img) -> str:
    return pytesseract.image_to_string(Image.open(img))
