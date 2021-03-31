import os,sys
from bs4 import BeautifulSoup

os.system('wget https://services.gradle.org/distributions/ -O Gradle_Distributions.html')
text = open(r'/data/foch/gradle/Gradle_Distributions.html', 'r+')
text.seek(0)

html = text.read()
bs_xml = BeautifulSoup(html,'html.parser')

#print(bs_xml.find_all("a"))
#print(bs_xml.find_all("span"))

# print(bs_xml.span.attrs)

# print(bs_xml.span.string)
# for item in bs_xml.find_all("span"):
#     print item.string



#print(bs_xml.a.string)


#print bs_xml.find('span',class_='name')

for item in bs_xml.find_all('span',class_='name'):
    #f = item.find(class_='name')
    print item.string
text.close()
