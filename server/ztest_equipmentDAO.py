# import instance of class
from zequipmentDAO import equipmentDAO

#create; values are category= %s, name= %s, supplier= %s, cost_eur=%
latestid = equipmentDAO.create(('Tier 1', 'Hammer T22', 'BBB', 2145.00))

# find by id
find_id = latestid # change it to look for a user specifed id
result = equipmentDAO.findByID(find_id);
print (result)

#update; values are category= %s, name= %s, supplier= %s, cost_eur=%
equipmentDAO.update(('Tier 2', 'Scanner', 'ccc', 555.12, latestid))
result = equipmentDAO.findByID(latestid);
print (result)

# get all 
allEquipment = equipmentDAO.getAll()
for equip in allEquipment:
  print(equip)

# delete
equipmentDAO.delete(latestid)
