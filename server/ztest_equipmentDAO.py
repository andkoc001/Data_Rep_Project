# import instance of class
from zequipmentDAO import equipmentDAO

#create
latestid = equipmentDAO.create(('Tier 1', 'Hammer T22', 'BBB', 2145.00))

# find by id
result = equipmentDAO.findByID(latestid);
print (result)

#update
equipmentDAO.update(('Fred',21,latestid))
result = equipmentDAO.findByID(latestid);
print (result)

# get all 
allEquipment = equipmentDAO.getAll()
for equip in allEquipment:
  print(equip)

# delete
equipmentDAO.delete(latestid)
