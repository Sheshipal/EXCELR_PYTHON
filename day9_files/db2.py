import pymysql

db = pymysql.connect(host='localhost', port = 3306, user = 'root', password = 'mysqlserverpassword@123', database = 'information')

if db:
	cursor = db.cursor()
	query = "insert into realestate values('NGO Colony', 'Warangal');"
	cursor.execute(query)
	print(cursor.rowcount,'record inserted')
	db.commit()
db.close()