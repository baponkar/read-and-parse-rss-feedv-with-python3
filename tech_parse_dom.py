from xml.dom import minidom
from xml.dom.minidom import parse
import requests


#url = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
#url = "https://tech.hindustantimes.com/rss/tech"
url = "http://feeds.bbci.co.uk/news/rss.xml"

resp = requests.get(url)
text = resp.text #getting xml content

fileobj = open("xml_file.xml",'wt') #creating xml file
fileobj.write(text)
fileobj.close()

DomTree = minidom.parse('xml_file.xml')#make ready to parse the data from xml file
collection = DomTree.documentElement

items = collection.getElementsByTagName('item') #taking all data inside of <item> attributes

for item in items:
    if item.hasAttribute("title"):
        print("Title :" + item.getAttribute("title"))

  
    link = item.getElementsByTagName('link')[0]
    print("link : " + link.childNodes[0].data)

    description = item.getElementsByTagName("description")[0]
    print("Description : " + description.childNodes[0].data)

    if item.hasAttribute("dc:creator"):
        creator = item.getElementsByTagName("dc:creator")[0]
        print("Creator : " + creator.childNodes[0].data)

    pubdate = item.getElementsByTagName("pubDate")[0]
    print("Pub date : " + pubdate.childNodes[0].data)

    if item.hasAttribute("media:content"):
        media_content = item.getElementsByTagName("media:content")
        print("Media content : " + media_content[0].attributes['url'].value)
    
        if item.hasAttribute("media:credit"):
            media_credit = item.getElementsByTagName("media:credit")[0]
            print("Media credit : " + media_credit.childNodes[0].data)

        else:
            print("Media credit : Null")
        if item.hasAttribute("media:description"):
            media_description = item.getElementsByTagName("media:description")[0]
            print("Media description : " + media_description.childNodes[0].data)
        else:
            print("Media description : Null")
    else:
        print("Media : Not supplied")

    print("===============================================================")

