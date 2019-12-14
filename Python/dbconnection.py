import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="mydatabase01")

print(mydb)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase01")


#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
	#print(x) 
 
#mycursor.execute("CREATE TABLE nivanika (name VARCHAR(255), age INT)")
'''
mycursor.execute("SHOW TABLES")

for x in mycursor:
	print(x) 
	'''
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("INSERT INTO nivanika(name,age) VALUES ('Nainika',2)")
#mycursor.execute("INSERT INTO nivanika(name,age) VALUES ('Nivaan',4)")

sql = "select * from Nivanika"
mycursor.execute(sql)