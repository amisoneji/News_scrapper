from pymongo import MongoClient
from flask_pymongo import PyMongo
from pymongo import MongoClient
import certifi
ca = certifi.where()
from flask_pymongo import PyMongo
client = MongoClient('mongodb+srv://root:root@cluster0.cgpw3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tls=True,tlsAllowInvalidCertificates=True)
print(client)
data_base="NewsDump"
db=client[data_base]
mng_db = client['db']
collection_name = 'InfoQ'
db_cm = mng_db[collection_name]
print(db_cm)
serchstring="Cloud"
db_cm.create_index([('Article Headline', 'text')])
boxs=db_cm.find({"$text": {"$search":"Cloud"}})

for box in boxs:
    print(box)
