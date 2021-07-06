from bs4 import BeautifulSoup
import scraper_functions
import requests
import smtplib
import pandas
import time
import csv
import os
        
# mail function that takes name, url and a dictionary of all the CHANGED attributes

def mail_funct(name, changeDict, url):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
                
        passwrd = os.environ.get('mail_pass')
        
        mailingList = ['choudharysiddharth01@gmail.com']
        smtp.login('choudharysiddharth01@gmail.com', passwrd)
        
        attributeChange = 'ATTRIBUTE             OLD             NEW'
        for key, value in changeDict.items():
            attributeChange = attributeChange + f'\n{key}             {value[0]}             {value[1]}'
        
        subject = f'Hi! There is an update regarding your product: {name}'
        body = f'your product: {name} \n has the following changes:\n{attributeChange}'
        msg = f'Subject: {subject}\n\n{body}'
        
        for mail in mailingList:
            smtp.sendmail('choudharysiddharth01@gmail.com', mail, msg.encode("utf-8"))
    
    
#function that checks the csv database for updating and alerting!    

def doCheck():
    with open('database.csv', 'r') as in_file:
        csv_reader = csv.reader(in_file)
        next(csv_reader)
    
        i=0
        # df = pandas.read_csv('database.csv', index_col=0, converters={'price in rupees' : str,
        #                                                          'rating' : str})
        for line in csv_reader:
            url = line[5]
            headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59"}
            
            r = requests.get(url, headers)
            htmlContent = r.content
            soup = BeautifulSoup(htmlContent, 'html.parser')
            
            newPrice = scraper_functions.getPrice(soup)
            newRating = scraper_functions.getRating(soup)
            newAvailability = scraper_functions.getAvailability(soup)
        
            changes = {}
            
            if int(line[2]) != newPrice:
                changes['price'] = [line[2], newPrice]
                
            if line[3] != newRating:
                changes['rating'] = [line[3], newRating]

            if line[4] != newAvailability:
                changes['availability'] = [line[4], newAvailability]
        
            df = pandas.read_csv('database.csv', index_col=0)
            df.at[i, 'price in rupees'] = newPrice
            df.at[i, 'rating'] = newRating
            df.at[i, 'availability'] = newAvailability
            i=i+1
            
            name = line[1]
            url=line[5]
            if changes:
                print(f'Change detected! Product:{line[1]} has new updates!')
                mail_funct(name, changes, url)
                df.to_csv("database.csv")
                print('database updated!')
            else:
                print(f'No change for Product:{line[1]}')
            time.sleep(2)

#doCheck()
if __name__ == '__main__':
    while 1:
        doCheck()
        time.sleep(7200)