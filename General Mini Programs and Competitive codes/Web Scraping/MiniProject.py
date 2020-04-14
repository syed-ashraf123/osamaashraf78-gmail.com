import requests
from random import choice
user=input('Please input any dta: ')
url='https://icanhazdadjoke.com/search'
res=requests.get(
	url,
	headers={'Accept':'application/json'},
	params={'term':user}
	)
res=res.json()
res=res['results']
len=len(res)
print(f"I'have got {len} jokes of {user}")
print("Here's One")
for i in res:
	print(i['joke'])
	break