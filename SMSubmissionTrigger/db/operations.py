
from datetime import datetime

def insert(collection_ref, client_id, data):
  data['_id'] = client_id
  current_dt = datetime.now().strftime("%d/%m/%Y %H:%m:%S")

  data['meta']['insert_datetime'] =current_dt
  data['meta']['shard'] = current_dt[-1:]
  x = collection_ref.insert_one(data)
  

# collection_ref : mycol = mydb["initial_assessment"]
def find_latest_client_record(collection_ref, client_id):
  
  myquery = { "_id": client_id}

  mydoc = collection_ref.find(myquery).sort([('_id',-1)]).limit(1)
  return mydoc




