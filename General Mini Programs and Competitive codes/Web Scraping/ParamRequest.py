import requests
url='https://icanhazdadjoke.com/search'
res=requests.get(url,headers={'Accept':'application/json'},
	params={'term':'cat'})
print(res.json())