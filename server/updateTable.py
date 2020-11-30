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
sql="UPDATE equipment SET name= %s, cost_eur=%s  where id = %s"
values = ("robot 1",3344.00, 1)

cursor.execute(sql, values)

db.commit()
print("Update done")