import dotenv
import os
import requests
import shutil

from bs4 import BeautifulSoup
from clean_email import clean_mail
from fetch_mail_from_pic import fetch_email_from_pic

dotenv.load_dotenv('./venv/.env')


def get_full_info(page_path):
    with open(page_path, 'r') as page:
        soup = BeautifulSoup(page, 'lxml')
        result = []
        name_elem = soup.find('h1', {'itemprop': 'name'})
        if name_elem is not None:
            name = name_elem.text
        else:
            print(page_path)
        result.append(name)
        branch = None
        try:
            branch = soup.find('div', {"id": "brBox"}).find('a', {"class": "br_link"}).find('span').text
            result.append(branch)
        except AttributeError:
            result.append(branch)
        street = soup.find('span', {'itemprop': 'streetAddress'}).text
        result.append(street)
        zip_code = soup.find('span', {'itemprop': 'postalCode'}).text
        result.append(zip_code)
        city = soup.find('span', {'itemprop': 'addressLocality'}).text
        result.append(city)
        woj = soup.find('span', {'itemprop': 'addressRegion'}).text
        result.append(woj)
        web_obj = soup.find_all('a', {'itemprop': 'url'})
        web = [w.text for w in web_obj]
        result.append(web)
        tel = soup.find_all('span', {'itemprop': 'telephone'})
        result.append([t.text for t in tel])
        email_obj = soup.find_all('img', {'class': 'emlImg'})
        email_links = [os.getenv('PART_URL').format(i.get('src')) for i in email_obj]
        email = []
        for i in email_links:
            req = requests.get(url=i, timeout=2, stream=True)
            with open(f"{os.getenv('PATH_TO_IMAGE').format(str(name).replace('/', '.'))}", "wb") as img:
                req.raw.decode_content = True
                shutil.copyfileobj(req.raw, img)
            email_to_clean = fetch_email_from_pic(f"{os.getenv('PATH_TO_IMAGE').format(str(name).replace('/', '.'))}")
            cleaned_email = clean_mail(email_to_clean)
            if not cleaned_email == "not_email":
                email.append(cleaned_email)
        result.append(email)
    return result


if __name__ == '__main__':
    print(get_full_info('./pages/page0.html'))
