from bs4 import BeautifulSoup
import requests


def parsing_html():
    r = requests.get('https://quotes.toscrape.com/')
    soup = BeautifulSoup(r.content, features='html.parser')

    articles = soup.findAll('quote')
    quote_list = []
    for a in articles:
        quote_list.append(a.find('itemprop').text)
    return soup
