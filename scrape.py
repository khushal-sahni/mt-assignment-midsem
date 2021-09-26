import requests
from bs4 import BeautifulSoup as bs


def scrape_webpage_get_words(page_number):
    url = 'https://dsal.uchicago.edu/cgi-bin/app/caturvedi_query.py?page='
    page_number = str(page_number)
    page = requests.get(url + page_number)
    soup = bs(page.content, 'html.parser')
    content = soup.find("div", {"class": "hw_result"}).get_text()
    read_data = content.splitlines()
    parsed = [word.split() for word in read_data]
    words_list = []
    for word in parsed:
        if len(word) > 0:
            words_list.append(word[0].split()[0])

    return words_list
