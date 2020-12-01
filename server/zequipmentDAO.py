import mysql.connector
import dbconfig as cfg
import json
from flask import jsonify

# create a class
class EquipmentDAO:
    db=""


    #def connectToDB(self): # in case the line below does not work
    def __init__(self):
        self.db = mysql.connector.connect(
        host = cfg.mysql['host'],
        user = cfg.mysql['user'],
        password = cfg.mysql['password'],
        database = cfg.mysql['database']
        )


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
        # convert data type from tuple to dictionary
        # results = cursor.fetchall()
        # results = dict(cursor.fetchall())
        # results = json.dumps(cursor.fetchall(), indent=4) # convert to json format
        # convert data type from tuple to dictionary
        returnArray = []
        #print(results)
        for result in results:
            # print(result)
            returnArray.append(self.convertToDictionary(result))
        cursor.close()
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="SELECT * FROM equipment WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        # convert to dictionary
        result = self.convertToDictionary(result)
        cursor.close()
        return result

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

    # Converting tuple returned from DB into dict (adapted from http://elizabethdaly.eu.pythonanywhere.com/)
    def convertToDictionary(self, result):
        
        # List of attributes - match html with colnames
        colnames = ['id', 'Category', 'name', 'supplier', 'price_eur', 'price_bc']
        
        # Empty list
        item = {}

        # Can't enumerate through an empty result, so check.
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value

        return item


# create instance of the class
equipmentDAO = EquipmentDAO()