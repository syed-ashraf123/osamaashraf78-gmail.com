import requests
nameList=[]
subList=[]
emailList=[]
expList=[]
Department=[]
newdept=[]
faculty='/Faculty.aspx'
from bs4 import BeautifulSoup
url='http://iul.ac.in/Department/'
path='Agriculture.aspx'
res=requests.get(f"{url}{path}")
soup=BeautifulSoup(res.text,'html.parser')
#print(soup)
li=soup.find(class_='nav nav-pills nav-stacked').find_all('li')
li.pop()
c=0
for i in li:
	#print('link:=',i)
	b=i.find('a')['href']
	if b=='IDPValuation.aspx':
		continue
	res=requests.get(f"{url}{b}")
	soup=BeautifulSoup(res.text,'html.parser')
	link=soup.find(class_='col-md-9').find_all('li')
	#print('Start of above loop')
	#print(link)
	#print('End of Above loop')
	for i in link:
		#print('Start of below loop')
		c=c+1
		if c==18 or c==20 or c==28:
			continue
		#print(c)
		#print(i)
		#print(i.find('a'))
		#print(i.find('a')['href'])
		ref=i.find('a')['href']
		dept=i.find('strong').get_text()
		Department.append(dept)
		print(f'Scraping=={dept} ')
		if ref=='http://iul.ac.in/CA/index.aspx':
			ref='http://iul.ac.in/CA'
		if ref=='http://iul.ac.in/PLYTCSPN/index.aspx':
			ref='http://iul.ac.in/PLYTCSPN'
		
		
		
		#print(f"{ref}")
		#print('End of BElow loop')
		res=requests.get(f"{ref}{faculty}")
		soup=BeautifulSoup(res.text,'html.parser')
		teach=soup.find_all(class_='teacher-item w-col w-col-4 w-dyn-item')
		for i in teach:
				name=i.find(class_='teacher-main-title').find('a').get_text()
				email=i.find(class_='job-title').get_text()
				email=email.replace('Email : ','')
				
				Expertise=i.find(class_='job-title').find_next_sibling().get_text()
				Expertise=Expertise.replace('Area of Expertise : ','')
				Subjects=i.find(class_='job-title').find_next_sibling().find_next_sibling().get_text()
				Subjects=Subjects.replace('Subject Taught : ','')
				nameList.append(name)
				subList.append(Subjects)
				newdept.append(dept)
				emailList.append(email)
				expList.append(Expertise)
import pandas as pd
df=pd.DataFrame({'Name':nameList,'Email':emailList,'Department':newdept,'Subjects':subList,'Expertise':expList})
df.to_csv('Faculty45.csv')
