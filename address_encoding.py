import urllib.request, urllib.parse, urllib.error
import json


address=input('Enter location: ')
print('Retrieving',address)
#Step 1: Accepts user input for location
print(urllib.parse.urlencode({'address':address}))
#step 2: Prints the location being retrieved and 
#step 3: Encodes the location as a URL-friendly string and prints it out.


