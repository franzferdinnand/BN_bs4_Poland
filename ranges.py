import ast
import dotenv
import os
import requests

from bs4 import BeautifulSoup

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
    req = requests.get(os.getenv('URL').format(1), proxies=ast.literal_eval(os.getenv("PROXY")), timeout=5)
    if req.status_code == 200:
        with open('temp.html', 'w') as file:
            file.write(req.text)

    with open('temp.html', 'r') as file:
        soup = BeautifulSoup(file, 'lxml')
        nums = soup.find('div', {'id': 'resBtNav'}).find('div', {'class': 'navLeft'}).text
        max_page = nums.split('z')[1].rstrip().replace(' ', '')
        # print(max_page[1].rstrip().replace(' ', ''))
    os.remove('temp.html')
    return int(max_page)


if __name__ == '__main__':
    print(ranges_for_parser(max_pages(), 30))
