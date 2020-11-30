import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  #user="datarep",  # this is the user name on my mac
  #passwd="password" # for my mac
  database="datarepresentation"
)

cursor = db.cursor()
sql="DELETE FROM equipment WHERE id = %s"
values = (1,)

cursor.execute(sql, values)

db.commit()
print("Delete done")