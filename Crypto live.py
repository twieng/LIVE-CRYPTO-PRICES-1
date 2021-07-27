from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.google.com/search?q=bitcoin+price'
HTML = requests.get(url)
soup = BeautifulSoup(HTML.text, 'html.parser')
print(soup.prettify())

#create a cuntion to get the price of a cryptocurrency
def get_crypto_price(coin):
    url = 'https://www.google.com/search?q=' +coin+ '+price'
    HTML = requests.get(url)
    soup = BeautifulSoup(HTML.text, 'html.parser')
    text = soup.find('div', attrs = {'class':"BNeawe iBp4i AP7Wnd"}).find('div', attrs={'class':"BNeawe iBp4i AP7Wnd"}).text
    return text

price = get_crypto_price('ethereum')
print(price)

def main():
    last_price = -1
    while True:
        crypto = 'ethereum'
        price = get_crypto_price(crypto)
        if price != last_price:
            print(crypto+' price: ', price)
            last_price = price
        time.sleep(3)
       
main()
