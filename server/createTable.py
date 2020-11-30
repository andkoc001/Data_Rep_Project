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
sql="CREATE TABLE equipment ( id INT PRIMARY KEY AUTO_INCREMENT, category ENUM ('Tier 1', 'Tier 2', 'Auxiliary', 'Spare') DEFAULT 'Tier 1', name VARCHAR(50), supplier VARCHAR(50), price_eur FLOAT(10, 2), price_bc FLOAT(8, 4) )"

cursor.execute(sql)