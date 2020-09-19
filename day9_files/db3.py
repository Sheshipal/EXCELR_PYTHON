import pymysql
import csv


db = pymysql.connect(host='localhost', port = 3306, user = 'root', password = 'mysqlserverpassword@123', database = 'information')

if db:
	cursor = db.cursor()
	with open('realestate.csv','r') as fileobj:
		reader = csv.reader(fileobj)
		for record in reader:
			city = record[1]
			street = record[0]
			query = "insert into realestate values('{}', '{}');".format(street,city)
			cursor.execute(query)
			
	print('insertion completed')
	db.commit()
db.close()