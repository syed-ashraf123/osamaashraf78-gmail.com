import requests
from bs4 import BeautifulSoup
res=requests.get('http://quotes.toscrape.com/',headers={'Accept':'application/json'})
resn=res.text
soup=BeautifulSoup(resn,'html.parser')
qt=soup.select('.text')
at=soup.select('.author')
for i,j in zip(qt,at):
	print(i.get_text())
	print(j.get_text())
page=soup.find(class_='next')

page=page.find('a')['href']

while resn:
	resn='http://quotes.toscrape.com/'
	resn=requests.get(f'{resn}{page}',headers={'Accept':'application/json'})
	resn=resn.text
	soup=BeautifulSoup(resn,'html.parser')
	qt=soup.select('.text')
	at=soup.select('.author')
	for i,j in zip(qt,at):
		print(i.get_text())
		print(j.get_text())
	page=soup.find(class_='next')
	if page:
		page=page.find('a')['href']
		print(page)