import mysql.connector
import dbconfig as cfg

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
        # convert data type from dupple to dictionary
        returnArray = []
        print(results)
        for result in results:
            print(result)
            #returnArray.append(self.convertToDictionary(result))
        cursor.close()
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="SELECT * FROM equipment WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        # convert to dictionary
        #result = self.convertToDictionary(result)
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

# create instance of the class
equipmentDAO = EquipmentDAO()