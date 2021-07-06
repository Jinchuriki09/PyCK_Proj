from bs4 import BeautifulSoup 
import scraper_functions
import requests
import pandas as pd
#import csv


def addEntry(url):
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59"}

    r = requests.get(url, headers)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    
    name = scraper_functions.getName(soup)
    price = scraper_functions.getPrice(soup)
    rating = scraper_functions.getRating(soup)
    availability = scraper_functions.getAvailability(soup)

    df = pd.read_csv('database.csv',index_col=0)
    newEntry = {'product name':name,
            'price in rupees':price,
            'rating':rating,
            'availability':availability,
            'link':url}

    df = df.append(newEntry, ignore_index=True)
    df.to_csv('database.csv')



# with open('database.csv', 'a', newline='') as in_file:
#     fieldnames = ['product_name', 'price in rupees', 'rating', 'link']
#     csv_writer = csv.writer(in_file)
    
#     row = [name, price, rating, availability, url]
#     csv_writer.writerow(row)