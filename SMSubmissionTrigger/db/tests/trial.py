from  SMSubmissionTrigger.db.operations import find_latest_client_record
from SMSubmissionTrigger.db import mydb


mycol = mydb["client_registration"]
rec = find_latest_client_record(mycol,'XXXLLLL719912')


from pprint import pprint


for document in rec: 
    pprint(document)
