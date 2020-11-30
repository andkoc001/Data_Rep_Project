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
sql="INSERT INTO equipment (category, name, supplier, price_eur) values (%s,%s,%s,%s)"
values = ("Tier 1", "CNC 1", "AAA", 1123.90)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

# for reference:
'''
CREATE TABLE equipment (
  id INT PRIMARY KEY AUTO_INCREMENT,
  category ENUM('Tier 1', 'Tier 2', 'Auxiliary', 'Spare') DEFAULT 'Tier 1',
  name VARCHAR(50),
  supplier VARCHAR(50),
  price_eur FLOAT(10, 2),
  price_bc FLOAT(8, 4)
);
'''