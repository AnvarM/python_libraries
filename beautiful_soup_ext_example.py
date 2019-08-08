from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://ramasanta.github.io/")
bsObj = BeautifulSoup(html)

tag_list = bsObj.findAll("div", {"class" : "project-name"})
print(tag_list) #print tag name with content

for tag in tag_list:
    print(tag.get_text()) #print just content