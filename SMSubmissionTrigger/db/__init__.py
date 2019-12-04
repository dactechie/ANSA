import json
from pprint import pprint
import pymongo
from ..config import ANSA_MONGO
from .operations import find_latest_client_record, insert


uri = ANSA_MONGO
client = pymongo.MongoClient(uri)

#print(client.list_database_names())
mydb = client["ansa"]
#mycol = mydb["initial_assessment"]

###############
# data = None
# with open("./b.json", "r") as file:
#   data = json.load(file)


###############