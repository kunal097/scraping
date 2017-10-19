from bs4 import BeautifulSoup as bs
import urllib
import urllib.request


url="https://twitter.com/realDonaldTrump"

page=urllib.request.urlopen(url)
soup=bs(page,"html.parser")
# print(soup.title.text)

# for link in soup.find_all('a'):
# 	print(link.get('href'))

a=soup.find('div',{'class':'js-tweet-text-container'})
print(a.find('p').text)