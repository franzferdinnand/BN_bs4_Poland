import ast
import dotenv
import os
import requests

dotenv.load_dotenv("./venv/.env")


def save_page(url_to_parse, path_to_save, proxy=ast.literal_eval(os.getenv("PROXY"))):
    req = requests.get(url=url_to_parse, proxies=proxy, timeout=15, stream=True)
    if not req.status_code == 200:
        print("ERROR: ", req.status_code)
    else:
        with open(f'{path_to_save}', "w") as page:
            page.write(req.text)
