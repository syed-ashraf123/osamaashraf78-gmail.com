from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import mysql.connector
import pickle
model=pickle.load(open('regressor_2latest22.pkl','rb'))
print(model)
mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  passwd="root",
  database="car_db"
)

class db:
	# def __init__(self,ii, name, last):
	# 	self.ii = ii
	# 	self.name = name
	# 	self.last = last
	# 	global mydb
	def data(self,year,km,ml,en,pwr,st,cm,ct,ty,tran,own):
		mycursor=mydb.cursor()
		sql="insert into car(years,km,ml,en,pwr,st,cm,ct,ty,tran,own) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s)"
		val = (year,km,ml,en,pwr,st,cm,ct,ty,tran,own)
		mycursor.execute(sql,val)
		mydb.commit()
app = Flask(__name__)

@app.route('/home',methods=['GET','POST'])
def home():
	print('dcdcdc')
	if (request.method=='POST'):
		def predict(year,km,ml,en,pwr,st,cm,ct,ty,tran,own):
			l=[year,km,ml,en,pwr,st]
			ll=["Ambassador","Audi","BMW","Bentley","Chevrolet","Datsun","Fiat","Force","Ford","Honda","Hyundai","Isuzu","Jaguar","Jeep","Lamborghini","Land","Mahindra","Maruti","Mercedes_Benz","Mini","Mitsubishi","Nissan","Porsche","Renault","Skoda","Tata","Toyota","Volkswagen","Volvo","Ahmedabad","Bangalore","Chennai","Coimbatore","Delhi","Hyderabad","Jaipur","Kochi","Kolkata","Mumbai","Pune","CNG","Diesel","LPG","Petrol","Automatic","Manual","First","Fourth_Above","Second","Third"]
			ll[ll.index(cm)]=1
			ll[ll.index(ct)]=1
			ll[ll.index(ty)]=1
			ll[ll.index(tran)]=1
			ll[ll.index(own)]=1
			for i in ll:
				if type(i)==str:
					ll[ll.index(i)]=0
			l.extend(ll)
			predict.x=model.predict([l])
			print(predict.x)
		year=request.form.get('year')
		km=request.form.get('km')
		ml=int(request.form.get('mileage'))
		en=int(request.form.get('engine'))
		pwr=int(request.form.get('power'))
		st=request.form.get('seats')
		cm=request.form.get('company')
		ct=request.form.get('city')
		ty=request.form.get('type')
		tran=request.form.get('trans')
		own=request.form.get('owner')
		predict(year,km,ml,en,pwr,st,cm,ct,ty,tran,own)
		ll=db()

		ll.data(int(year),int(km),int(ml),int(en),int(pwr),st,cm,ct,ty,tran,own)
		return render_template('front.html',show_results=round(predict.x[0],2))
	else:
		return render_template('front.html')

app.run(debug=True)