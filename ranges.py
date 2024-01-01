import ast
import dotenv
import os
import requests

from bs4 import BeautifulSoup
from numpy.core.defchararray import isnumeric

dotenv.load_dotenv('./venv/.env')


def ranges_for_parser(num_of_pages, step):
    start = 0
    stop = 0
    ranges = [(0, step)]
    for i in range(0, num_of_pages):
        start += step
        stop = start + step
        if stop <= num_of_pages:
            ranges.append((start, stop))
    return ranges


def max_pages():
    req = requests.get(os.getenv('URL').format(os.getenv("WOJEWÓDZTWO"),1), proxies=ast.literal_eval(os.getenv("PROXY")), timeout=5)
    if req.status_code == 200:
        with open('temp.html', 'w') as file:
            file.write(req.text)

    with open('temp.html', 'r') as file:
        soup = BeautifulSoup(file, 'lxml')
        nums_mod = soup.find('span', {'class': 'disabled'}).find_all('a', {'class': 'pgn'})
        nums = [int(i.text) for i in nums_mod if isnumeric(i.text)]
        max_page = max(nums)

    os.remove('temp.html')
    return int(max_page)
