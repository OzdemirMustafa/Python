import pymongo


client = pymongo.MongoClient("mongodb+srv://ozdemirmustafa:4cVGqpFO8HEPNJWQ@mymondodb-wojt8.mongodb.net/py-app?retryWrites=true&w=majority")
db = client["py-app"]
mycollection = db["products"]
product = {"name": "Iphone 11S","price" : "10000"}
productList =[
  {"name": "Iphone XS","price" : "11000"},
  {"name": "Iphone 11","price" : "8800"},
  {"name": "Iphone 12","price" : "13000"},
  {"name": "Iphone 9","price" : "14000"},
  {"name": "Iphone 9S","price" : "8000"}
]

#result = mycollection.insert_many(productList)
#findelement = mycollection.find_one()
#for i in mycollection.find({},{"_id": 0}):
# print(i)

filters = mycollection.find({

"name": {
    "$in" : ["Iphone 11S"]
}

})
'''
prices = mycollection.find({
    "price": {
       "$gte": "9000"
    }
})
'''

for i in filters:
  print(i)