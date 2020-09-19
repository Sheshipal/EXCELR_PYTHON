import pymysql

db = pymysql.connect(host='localhost', port = 3306, user = 'root', password = 'mysqlserverpassword@123', database = 'information')

if db:
	cursor = db.cursor()
	query = 'select * from realestate'
	cursor.execute(query)
	for record in cursor.fetchall():
		print(record)

db.close()