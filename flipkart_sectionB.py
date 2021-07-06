from flipkart_page import addEntry
from bs4 import BeautifulSoup
import requests
#import time

def populateDB(url):
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59"}

# U L     R C S I G
#  R    P  O E S N

    r = requests.get(url, headers)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
            
    data = soup.find_all('div', class_="_13oc-S")
    
    product_class = data[0].contents[0].div['class'][0]
        
    links = soup.find_all('div', class_=product_class)

    #i = 1
    for link in links:
        product_link = 'https://flipkart.com' + link.find('a')['href']
        # print(i)
        # i+=1
        addEntry(product_link)
        #time.sleep(1)