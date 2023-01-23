#geojason.py
import urllib.request, urllib.parse, urllib.error
import json


serviceurl =input("enter location url: ")#http://py4e-data.dr-chuck.net/comments_1705780.json
print("Retriving: ",serviceurl)

uh=urllib.request.urlopen(serviceurl)
data=uh.read().decode()
print("retrived characters=",len(data))

try:
    js=json.loads(data)
except:
    print("Problem with json file or some other error as there is no json file found")
print("count: ",len(js["comments"]))
sum=0
for i in range(len(js["comments"])):
    no=js["comments"][i]["count"]
    sum=sum+no
print("the sum is: ",sum)
'''
Retrieve the JSON data from the specified URL using the urllib library's urlopen function and decode the data to a string.
Parse the JSON data using the json.loads function and handle any errors that may occur.
Iterate through the "comments" key in the parsed JSON data and extract the "count" values and sum them.
'''
         
    



