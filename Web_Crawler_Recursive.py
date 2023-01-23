import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl, sys


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def linkf(url, count, position):
    if count > 0:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        link=[]
        tags = soup('a')
        for tag in tags:
            link.append(tag.get('href',None))
        print("Retrieving",link[position-1])
        linkf(link[position-1], count-1, position)
    else:
        print("Final URL:", url)

count = int(input('Enter count: '))
position = int(input('Enter position: '))
url=input('Enter the Url: ')
#http://py4e-data.dr-chuck.net/known_by_Hajra.html

linkf(url, count, position)

'''
Retrieve HTML data from a specified URL
Use BeautifulSoup to parse the HTML data
Extract the 'href' attribute values of the 'a' tags in the HTML data
Repeat step 1 to 3 a specified number of times, using the 'href' values as the new URLs
Print the final URL after the specified number of iterations'''










    