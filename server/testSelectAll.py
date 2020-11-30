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
sql="SELECT * FROM equipment"
values = (1,) # there is comma, because it must be a tupple

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
  print(x)

