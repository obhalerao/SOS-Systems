#Gabi Tessier, 7/19/2019
#This creates a database with MongoDB with PyMongo
import pymongo
from bson.objectid import ObjectId
import gridfs
from bson import objectid



#uploadphoto , downloadphoto
class RemSensDB():
    db = None
    fs = None

    #creats the database
    def DataBaseInitialize(self):
        # run code that opens the database and stores it as an object
        pass

    def insertData(self, js):
        # insert data into the database
        # the data is in a JSON format https://www.w3schools.com/js/js_json_intro.asp
        pass

    def findByID(self, id_number):
        # given the id number of a MongoDB element, return the entry in the database
        pass


    def findByName(self, n):
        # given the name of an image in the database
        # return the database entry
        pass

    # store the data in the database. Returns the id of the file in gridFS
    def uploadphoto(self, b, name):
        # insert inputted data into the database
        pass

    def downloadphoto(self, a):
        # given a database entry
        # return the enclosed image file
        pass

    def __init__(self):
        self.DataBaseInitialize()
        #self.insertData()

if __name__ == "__main__":
    # test data
    
    mongo_database = RemSensDB()

    name = "image1"
    id_number = "5d31ceeff814e0b3a9fe59de"
    filename = "images/"

    mongo_database.findByName(name)
    mongo_database.findByID(id)
    # mongo_database.uploadphoto(filename,name)
    # mongo_database.downloadphoto(mongo_database.uploadphoto(filename))
