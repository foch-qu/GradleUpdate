import os,sys
from bs4 import BeautifulSoup

os.system('wget http://download.cidana.com/distributions/ -O Index_of_distributions.html')
text = open(r'/data/foch/gradle/Index_of_distributions.html', 'r+')
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
for item in bs_xml.find_all("a"):
    f = item.string
    print (f)
text.close()