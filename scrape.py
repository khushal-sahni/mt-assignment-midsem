import requests
from bs4 import BeautifulSoup as bs
from pathlib import Path


def scrape_webpage_store_in_files():
    target_path = Path('scrapped_files')
    target_path.mkdir(parents=True, exist_ok=True)
    url = 'https://dsal.uchicago.edu/cgi-bin/app/bahri_query.py?page='

    for i in range(709):
        page = requests.get(url + str(i))
        soup = bs(page.content, 'html.parser')
        content = soup.find("div", {"class": "hw_result"}).get_text()
        with open('scrapped_files/' + str(i + 1) + '.txt', 'a') as file:
            file.write(content)
