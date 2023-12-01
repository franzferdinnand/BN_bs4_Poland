import ast
import os
import requests
import shutil


def save_email_pic(url_img, filename):
    req = requests.get(url=url_img, proxies=ast.literal_eval(os.getenv("PROXY")), timeout=2, stream=True)
    if req.status_code == 200:
        with open(f"./img/email_{str(filename).replace('/', '.')}.png", "wb") as file:
            req.raw.decode_content = True
            shutil.copyfileobj(req.raw, file)
