import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url
        print("starting Scraper")


    def get_data(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        return(soup)

    def parse(soup):
        products_list = []
        results = soup.find_all('div', {'class': 's-item__info clearfix'})
        for item in results:
            if (item.find('a', {'class': 's-item__link'})['href'] != "https://ebay.com/itm/123456?hash=item28caef0a3a:g:E3kAAOSwlGJiMikD&amdata=enc%3AAQAHAAAAsJoWXGf0hxNZspTmhb8%2FTJCCurAWCHuXJ2Xi3S9cwXL6BX04zSEiVaDMCvsUbApftgXEAHGJU1ZGugZO%2FnW1U7Gb6vgoL%2BmXlqCbLkwoZfF3AUAK8YvJ5B4%2BnhFA7ID4dxpYs4jjExEnN5SR2g1mQe7QtLkmGt%2FZ%2FbH2W62cXPuKbf550ExbnBPO2QJyZTXYCuw5KVkMdFMDuoB4p3FwJKcSPzez5kyQyVjyiIq6PB2q%7Ctkp%3ABlBMULq7kqyXYA"):
                # strip bids to make it an integer
                raw_bid = item.find('span', {'class': 's-item__bids'}).text
                bid_int = ""
                for i in range(len(raw_bid)):
                    if (raw_bid[i].isdigit()):
                        bid_int += raw_bid[i]
                
                product = {
                    'title': item.find('div', {'class': 's-item__title'}).text.replace('New listing', ''),
                    'price': float(item.find('span', {'class': 's-item__price'}).text.replace('£', '').replace(',', '').strip()),
                    'time_left': item.find('span', {'class': 's-item__time-left'}).text,
                    'bids': int(bid_int),
                    'link': item.find('a', {'class': 's-item__link'})['href']
                }
                products_list.append(product)
        return products_list

    def return_data(self):
        soup = Scraper.get_data(self.url)
        # print(type(Scraper.parse(soup))) # dictionary inside list
        # print("\n\n")
        # print(Scraper.parse(soup)[0].get('title'))
        # print(Scraper.parse(soup)[0].get('price'))
        # print(Scraper.parse(soup)[0].get('time_left'))
        # print(Scraper.parse(soup)[0].get('bids'))
        # print(Scraper.parse(soup)[0].get('link'))

        return Scraper.parse(soup)
        # return Scraper.parse(soup)[0].get('title')