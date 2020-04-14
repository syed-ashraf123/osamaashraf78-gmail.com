
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
a=soup.body.contents
print(a)
print(a[1])
a=soup.body.font.next_sibling.find_next_sibling()#previous_sibling also a fn 
print(a)
soup.body.font.next_sibling.find_next_sibling(class_='second')#previous_sibling also a fn 
print(a)
