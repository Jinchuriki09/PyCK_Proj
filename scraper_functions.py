#single link scraping functions start

def getName(soup):
    productName = soup.find('span', class_="B_NuCI").text
    return productName

def getPrice(soup):
    productPrice = soup.find('div', class_="_30jeq3 _16Jk6d").text[1:]
    return int(productPrice.replace(',',''))

def getRating(soup):
    if(soup.find('div', class_="_3LWZlK") == None):
        return 'no rating yet'
    else:
        productRating = soup.find('div', class_="_3LWZlK").text
        return productRating
    
def getAvailability(soup):
    if(soup.find('div', class_="_16FRp0") == None):
        return 'available'
    else:
        return 'not available'
    
#single link scraping functions end
