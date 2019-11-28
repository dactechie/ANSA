import json

from pprint import pprint
import pymongo
from .operations import find_latest_client_record, insert

uri = "mongodb://ansa-mongo-inst:WGZ9Yl2iSCo6lOcKOeqDnjzhlBs2Pi6n8EgSXaOioXrKZJMLUhIa4Q92E91gJFfHESSydrAn4VdIYgSjZKhhJA==@ansa-mongo-inst.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@ansa-mongo-inst@&retrywrites=false"
client = pymongo.MongoClient(uri)

#print(client.list_database_names())
mydb = client["ansa"]
#mycol = mydb["initial_assessment"]

###############
# data = None
# with open("./b.json", "r") as file:
#   data = json.load(file)


###############