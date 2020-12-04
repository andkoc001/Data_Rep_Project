import mysql.connector
import server.dbconfig as cfg
import json
from flask import jsonify

# create a class
class EquipmentDAO:
    
    db=""

    def connectToDB(self): # in case the line below does not work
        self.db = mysql.connector.connect(
            host = cfg.mysql['host'],
            user = cfg.mysql['user'],
            password = cfg.mysql['password'],
            database = cfg.mysql['database']
        )

    def __init__(self):
        self.connectToDB()

    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

    def create(self, values):
        cursor = self.db.cursor()
        sql="INSERT INTO equipment (category, name, supplier, price_eur) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)
        cursor.close()
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="SELECT * FROM equipment"
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        returnArray = []
        for result in results:
            # print(result)
            # convert data type from tuple to dictionary
            returnArray.append(self.convertToDictionary(result))
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="SELECT * FROM equipment WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        # convert result to dictionary and return
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="UPDATE equipment SET category= %s, name= %s, supplier= %s, price_eur= %s  WHERE id = %s"
        cursor.execute(sql, values)
        cursor.close()
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql="DELETE FROM equipment WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        print("Delete done")

    # Converting tuple returned from DB into dictionary
    def convertToDictionary(self, result):        
        # List of attributes - match html with colnames
        colnames = ['id', 'category', 'name', 'supplier', 'price_eur']        
        # Empty dict
        item = {}
        # if result exist, enumerate through
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item


# create instance of the class
equipmentDAO = EquipmentDAO()