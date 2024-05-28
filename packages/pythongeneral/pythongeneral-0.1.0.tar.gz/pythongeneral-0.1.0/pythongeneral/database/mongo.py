import pymongo

class MongoCURD:
    def __init__(self,mongo_db,mongo_collection) -> None:
        self.db = mongo_db
        self.collection = mongo_collection
    def insert_one(self,insert_data):
        self.db[self.collection].insert_one(insert_data)
    def insert_many(self,inserts_data):
        self.db[self.collection].insert_many(inserts_data)
    def insertOneData(self, data):
        self.db[self.collection].insert_one(data)
    def insertManyData(self, data):
        self.db[self.collection].insert_many(data)
    def findOneData(self, data):
        findData = self.db[self.collection].find_one(data)
        return findData
    def findManyData(self, data):
        findData = self.db[self.collection].find(data)
        return findData
    def findAllData(self):
        findData = self.db[self.collection].find()
        return findData

    def findGeometryData(self,findCoordinate,findDistance):
        findDict = {}
        location = {}
        nearSphere = {}
        geometry = {}
        geometry["type"] = "Point"
        geometry["coordinates"] = findCoordinate
        nearSphere["$geometry"] = geometry
        nearSphere["$maxDistance"] = findDistance
        location["$nearSphere"] = nearSphere
        findDict["location"] = location
        findData = self.db[self.collection].find(findDict)
        return findData

    def updateOneData(self,findData,updateData):
        self.db[self.collection].update_one(findData,updateData)

    def updateManyData(self,findData,updateData):
        self.db[self.collection].update_many(findData,updateData)

    def deleteOneData(self,data):
        self.db[self.collection].delete_one(data)

    def deleteManyData(self,data):
        self.db[self.collection].delete_many(data)