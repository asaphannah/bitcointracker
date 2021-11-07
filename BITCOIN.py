#Bitcoin price tracker in real time

#Import libraries
from bs4 import BeautifulSoup
import requests
import time

#Get the URL that contains price.
url = 'http://www.google.com/search?q=bitcoin+price'

#Make a request to the website
HTML = requests.get(url)

#Parse the HTML
soup = BeautifulSoup(HTML.text, 'html.parser')

#print soup to find where the text is for the price
print(soup.prettify())



#Create a function that gets the price
def get_crypto_price(coin):
    #Get the URL that contains price.
    url = 'http://www.google.com/search?q=bitcoin+price'
    
    #Make a request to the website
    HTML = requests.get(url)
    
    #Parse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser')
    
    #Find the current price
    text = soup.find('div', attrs={'class' : 'BNeawe iBp4i AP7Wnd'}).find('div', attrs={'class' : 'BNeawe iBp4i AP7Wnd'}).text
    
    #return the text
    return text

#get the price of a crypto
price = get_crypto_price('bitcoin')

#print the price
print(price)


#create a function to show price as it changes
def main():
    last_price = -1
    #Create a loop to continuously update price
    while True:
        #Choose the cryptocurrency to get price of
        crypto = 'bitcoin'
        #Get price
        price = get_crypto_price(crypto)
        #check if price changed
        if price != last_price:
            print(crypto+ ' price: ', price)
            last_price = price
        time.sleep(1)
        #Run
        
        
