import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="library"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE Officers (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("SHOW TABLES")
mycursor.execute("INSERT INTO Officers(name,address) VALUES('Arun','abcde')")

print(mycursor.rowcount,"record insered")




class Welcome:
	def __init(self,frt):
		name=frt

	def login():
		print("haii")


w1=welcome("orange")
w1.login()



class WelBack(Welcome):
	super().__init__()