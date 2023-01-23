#Beautiful soup
#input-https://bidhideb-com.webflow.io/
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

import ssl 
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("enter the url: ")
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html, 'html.parser')#filtered html,html.praser is also a function inside BS4

#searching all the link inside <a> tag, all the reference link in that webpage
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))

# searching all the sorce of <img) tags
tags=soup('img')
for tag in tags:
    print(tag.get('src',None))



#output:
'''
mailto:Bidhideb.Ghosh@hotmail.com?subject=I%20am%20interested%20to%20work%20with%20you%3B
/#Portfolio
https://www.linkedin.com/in/bidhideb-ghosh-316601197/
/
#Portfolio
/project/remote-work-web-design
/project/remote-work-web-design
/project/invade
/project/invade
/project/allsafe
/project/allsafe
/project/ski-club-website
/project/ski-club-website
/project/astro-virtual-summit
/project/astro-virtual-summit
https://webflow.com/
mailto:Bidhideb.Ghosh@hotmail.com?subject=I%20am%20interested%20to%20work%20with%20you%3B
https://uploads-ssl.webflow.com/5f2a87c0e56633f0240543c9/5f2be7494d83a025f754696a_Group%206.svg
https://uploads-ssl.webflow.com/5f2a87c03bdc137faaa7e806/5f2d99eedcdca6be23ca88f1_Chat%20App.jpg
https://uploads-ssl.webflow.com/5f2a87c0e56633f0240543c9/5f2a87c03bdc131de6a7e7fe_dot%20pattern-min.png
https://uploads-ssl.webflow.com/5f2a87c0e56633f0240543c9/5f2a87c03bdc139732a7e7fd_ic-arrow-forward-18px.svg
https://uploads-ssl.webflow.com/5f2a87c03bdc137faaa7e806/606926c9d28c5c585c9a769d_Group%2015.png
https://uploads-ssl.webflow.com/5f2a87c0e56633f0240543c9/5f2a87c03bdc131de6a7e7fe_dot%20pattern-min.png
https://uploads-ssl.webflow.com/5f2a87c0e56633f0240543c9/5f2a87c03bdc139732a7e7fd_ic-arrow-forward-18px.svg
https://uploads-ssl.webflow.com/5f2a87c03bdc137faaa7e806/60692dcebd1846bc4fef735f_allsafe-min.png
https://uploads-ssl.webflow.com/5f2a87c0e56633f0240543c9/5f2a87c03bdc131de6a7e7fe_dot%20pattern-min.png
https://uploads-ssl.webflow.com/5f2a87c0e56633f0240543c9/5f2a87c03bdc139732a7e7fd_ic-arrow-forward-18px.svg
https://uploads-ssl.webflow.com/5f2a87c03bdc137faaa7e806/5f2dae015caf87ee528e525d_ts%20ok-min.jpg
https://uploads-ssl.webflow.com/5f2a87c0e56633f0240543c9/5f2a87c03bdc131de6a7e7fe_dot%20pattern-min.png
https://uploads-ssl.webflow.com/5f2a87c0e56633f0240543c9/5f2a87c03bdc139732a7e7fd_ic-arrow-forward-18px.svg
https://uploads-ssl.webflow.com/5f2a87c03bdc137faaa7e806/5f2d9de5ef3e384f7d1abb25_Chat%20App%20(1)-min.jpg
https://uploads-ssl.webflow.com/5f2a87c0e56633f0240543c9/5f2a87c03bdc131de6a7e7fe_dot%20pattern-min.png
https://uploads-ssl.webflow.com/5f2a87c0e56633f0240543c9/5f2a87c03bdc139732a7e7fd_ic-arrow-forward-18px.svg
https://uploads-ssl.webflow.com/5f2a87c0e56633f0240543c9/5f2aefe7216cee2904078dcd_5b64896607daaa6aea1e208f_design.jpg
https://uploads-ssl.webflow.com/5f2a87c0e56633f0240543c9/5f2af0df31a93152be6d7b04_5b64896678f5c5a74226a224_webflow.jpg
https://uploads-ssl.webflow.com/5f2a87c0e56633f0240543c9/5f2af0df106a6eb94319fc08_5b648966d2f71f7f19f5a170_landing.jpg

'''