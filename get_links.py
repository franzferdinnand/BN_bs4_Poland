import dotenv
import os

from bs4 import BeautifulSoup

dotenv.load_dotenv("./venv/.env")


def get_links(page) -> list:
    result = []
    with open(page, 'r') as page:
        soup = BeautifulSoup(page, 'lxml')
        links = soup.find_all('a', {"class": "wizLnk"})
        for link in links:
            result.append(link.get("href"))

    return result


if __name__ == '__main__':
    x = get_links(os.getenv("PATH_TO_SAVED_LINKS").format('151'))
