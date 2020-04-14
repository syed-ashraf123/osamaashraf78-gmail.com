html='''<html>
<head>
	<style>
		P
		{
			color: green;

		}
	</style>
</head>
<body>
My Mother has <font color="blue">blue</font>  eyes.<br>
My Mother has <P>blue</P>  eyes.<br>
<div>My Mother has <Span style="color: blue;">blue</Span>  eyes.</div>
<div color='red'>My Has has <Span style="color: blue;">blue</Span>  eyes.</div>
<ul>
<li id='first'>ok</li>
<li class='second'>bye</li>
<li class='second'>good</li>
</ul

</body>
</html>'''
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'html.parser')
#print(soup)
#print(type(soup))
#print(soup.body)
#print(soup.body.div)

#print(soup.find('div'))
#print(soup.find_all('div'))
#print(soup.find_all('li'))


#print(soup.find(id='first'))
#print(soup.find_all(class_='second'))
print(soup.find_all(attrs={'color':'red'}))