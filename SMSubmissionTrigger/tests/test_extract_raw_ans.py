
import json
import pprint
from SMSubmissionTrigger.survey_monkey.response_extractor import extract_response
from SMSubmissionTrigger.utils.constants import survey_type
from SMSubmissionTrigger.db import mycol, insert, find_latest_client_record


def findlatest(client_id):
  last = find_latest_client_record(mycol, client_id)
  for x in last:
    print(x)


def test_extract(survey_id):

  stype = survey_type[survey_id]

  #schfname = f"SMSubmissionTrigger/json/{stype}_schema.json"
  if stype.qna_map_key is 'initial_assessment' :
    from SMSubmissionTrigger.schema.initial_assessment_schema import schema as schema_json
    #from SMSubmissionTrigger.schema.matrix_aod_history import schema as schema_json
    #from SMSubmissionTrigger.schema.text_matrix_rating_other import schema as schema_json
    
  else:
    from SMSubmissionTrigger.schema.client_registration_schema import schema as schema_json

  
  respfname = f"SMSubmissionTrigger/tests/initial_assessment_generated_response2.json"
  #respfname = f"SMSubmissionTrigger/tests/matrix_rating_other.json"
  #respfname = f"SMSubmissionTrigger/tests/client_registration_response2.json"
  survey_response = None
  with open(respfname, "r") as file:
    survey_response = json.load(file)
  
  raw_answers, errors = extract_response(schema_json, answers_json=survey_response, stype=stype)
  return raw_answers, errors
  

def process(data):
  with open("b.json", "w") as wrfile:
    json.dump(data, wrfile)
  #pprint.pprint(data)
  

def insert_data(data):
  client_id = data['DEMOGRAPHICS']['client_id']  
  insert(mycol, client_id ,data)



if __name__ == "__main__":
    #survey_id = "271875304"
    survey_id = "271604360"

    data , errors = test_extract(survey_id)    
    #pprint.pprint(data)
    
    process(data)

    #insert_data(data)
    
    #id = "Q5553D234991" 
    #id = "AFTUT23232321"

    #findlatest(id)
    