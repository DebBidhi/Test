import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')#http://py4e-data.dr-chuck.net/comments_1705779.xml
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
#print(data.decode()),full xml file

print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

Nolist=tree.findall('.//count')
print('Count:', len(Nolist))
sum=0

for no in Nolist:
    sum=sum+int(no.text)
print('the sum of all thoe count is :',sum)


'''
Retrieve XML data from a specified URL
Parse the XML data into an xml tree
Count the number of elements with the tag 'count' in the XML tree
Sum the values of the text in all elements with the tag 'count'
'''

