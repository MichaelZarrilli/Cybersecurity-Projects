import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="NaH32@4GKL6#My",
	database="testdatabase"
	)

mycursor = db.cursor()

#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
mycursor.execute("INSERT Person (name, age) VALUES(%s,%s)", ("Joe", 22))
#db.commit()
#mycursor.execute()

mycursor.execute("SELECT * FROM Person")

for x in mycursor:
	print(x)

