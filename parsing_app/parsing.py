from bs4 import BeautifulSoup
from datetime import datetime
import requests

from parsing_app.models import Author, Quote


def parsing_html():

    counter = 5     # count of quotes to add
    quote_list = []

    r = requests.get('https://quotes.toscrape.com/')
    soup = BeautifulSoup(r.content, features='html.parser')

#     while counter:

    articles = soup.findAll('div', class_="quote")

    for a in articles:
        # Parsing author detail page
        auth = requests.get('https://quotes.toscrape.com' + a.find('a').get('href'))
        s_auth = BeautifulSoup(auth.content, features='html.parser')
        author_tpl = Author.objects.get_or_create(name=a.find('small', class_='author').text,
                                                  birth_date=datetime.strptime(
                                                      s_auth.find('span', class_='author-born-date').text, "%B %d, %Y"),
                                                  birth_place=s_auth.find('span',
                                                                          class_='author-born-location').text[3:],
                                                  description=s_auth.find('div', class_='author-description').text)

        qt = a.find('span', class_='text').text
        quote_tpl = Quote.objects.get_or_create(text=qt, author=author_tpl[0])
        if quote_tpl[1]:
            quote_list.append(author_tpl[0].name + ': ' + quote_tpl[0].text)
            counter -= 1
            if counter == 0:
                break

    if counter:
        next_ref = soup.find('li', class_="next")
        print(next_ref)

    return quote_list
