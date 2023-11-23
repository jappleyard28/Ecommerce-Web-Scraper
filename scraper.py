import requests
from bs4 import BeautifulSoup

url = "https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw=cars&_sacat=0&rt=nc&LH_Auction=1"

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    return(soup)

def parse(soup):
    products_list = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        if (item.find('a', {'class': 's-item__link'})['href'] != "https://ebay.com/itm/123456?hash=item28caef0a3a:g:E3kAAOSwlGJiMikD&amdata=enc%3AAQAHAAAAsJoWXGf0hxNZspTmhb8%2FTJCCurAWCHuXJ2Xi3S9cwXL6BX04zSEiVaDMCvsUbApftgXEAHGJU1ZGugZO%2FnW1U7Gb6vgoL%2BmXlqCbLkwoZfF3AUAK8YvJ5B4%2BnhFA7ID4dxpYs4jjExEnN5SR2g1mQe7QtLkmGt%2FZ%2FbH2W62cXPuKbf550ExbnBPO2QJyZTXYCuw5KVkMdFMDuoB4p3FwJKcSPzez5kyQyVjyiIq6PB2q%7Ctkp%3ABlBMULq7kqyXYA"):
            product = {
                'title': item.find('div', {'class': 's-item__title'}).text,
                'soldprice': float(item.find('span', {'class': 's-item__price'}).text.replace('£', '').replace(',', '').strip()),
                'timeleft': item.find('span', {'class': 's-item__time-left'}).text,
                'bids': item.find('span', {'class': 's-item__bids'}).text,
                'link': item.find('a', {'class': 's-item__link'})['href']
            }
            products_list.append(product)
    return products_list

'''def output(products_list):
    productsdf = pd.DataFrame(products_list)
    productsdf.to_csv('output.csv', index=False)
    print("saved to csv")
    return'''

soup = get_data(url)
print(parse(soup)[0].get('title'))