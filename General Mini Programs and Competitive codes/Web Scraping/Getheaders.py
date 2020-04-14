import requests
url='https://icanhazdadjoke.com'
#res=requests.get(url,headers={'Accept':'text/plain'})#Will get plain text only from this.Not all websotes supports it
#print(res.text)

res=requests.get(url,headers={'Accept':'application/json'})#Json converts plain text to a dictionary which we can use it in our python programming
print(res.text)#This gives dictionary in string "Dictionatry"
print(res.json())#It gives only dictionary  Dictionary