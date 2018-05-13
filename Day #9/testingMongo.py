from pymongo import MongoClient

client = MongoClient("mongodb://pytest:test@ds237848.mlab.com",37848)
db = client["first"]
#db.authentication("pytest","test")
classes = db.raspored
print(str(classes.find()))