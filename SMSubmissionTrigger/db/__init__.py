import json
from datetime import datetime
from pprint import pprint
import pymongo

uri = "mongodb://ansa-mongo-inst:WGZ9Yl2iSCo6lOcKOeqDnjzhlBs2Pi6n8EgSXaOioXrKZJMLUhIa4Q92E91gJFfHESSydrAn4VdIYgSjZKhhJA==@ansa-mongo-inst.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@ansa-mongo-inst@&retrywrites=false"
client = pymongo.MongoClient(uri)

#print(client.list_database_names())
mydb = client["ansa"]
mycol = mydb["initial_assessment"]

data = None
with open("./b.json", "r") as file:
  data = json.load(file)

data['DEMOGRAPHICS']['ClientID'] ='Q5553D234991'
data['_id'] = data['DEMOGRAPHICS']['ClientID']

data['meta']['insert_datetime'] = datetime.now().strftime("%d/%m/%Y %H:%m:%S")

data['meta']['shard'] = data['meta']['insert_datetime'][-1:]
x = mycol.insert_one(data)


# mydict = { "DEMOGRAPHICS":{"ClientID": "ASF44334332321"}, "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)

pprint(x)
#x = mycol.find_one()

#myquery = { "address": { "$gt": "S" } }

# myquery = { "DEMOGRAPHICS.ClientID": "ZZ44334332321" }
# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)




