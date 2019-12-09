
import json
import pprint
from SMSubmissionTrigger.survey_monkey.response_extractor import extract_response
from SMSubmissionTrigger.utils.constants import survey_type
from SMSubmissionTrigger.db import mydb, insert, find_latest_client_record
from SMSubmissionTrigger.utils.scores_answers import get_total_score


def findlatest(collection_ref, client_id):
  last = find_latest_client_record(collection_ref, client_id)
  for x in last:
    print(x)


def extract(survey_id):

  stype = survey_type[survey_id]
  respfname = None
  #schfname = f"SMSubmissionTrigger/json/{stype}_schema.json"
  if stype.qna_map_key is 'initial_assessment' :
    from SMSubmissionTrigger.schema.initial_assessment_schema import schema as schema_json
    respfname = f"SMSubmissionTrigger/tests/initial_assessment_generated_response2.json"
    ## TODO add logic
    # if there was no registration done recently (__or if ep was marked as closed__), 
    # then return error with advice: that have to  register first
    # otherwise get the ClientREgistration ID from Mongo and stick it into the mongo and CDS IntialAssessment object
    
    # Similarly,if there was no InitialAssessment, can't do ITSP review.

    #from SMSubmissionTrigger.schema.matrix_aod_history import schema as schema_json
    #from SMSubmissionTrigger.schema.text_matrix_rating_other import schema as schema_json
    
  else:
    from SMSubmissionTrigger.schema.client_registration_schema import schema as schema_json
    respfname = f"SMSubmissionTrigger/tests/client_registration_response2.json"


  #respfname = f"SMSubmissionTrigger/tests/matrix_rating_other.json"

  survey_response = None
  with open(respfname, "r") as file:
    survey_response = json.load(file)
  
  raw_answers, errors = extract_response(schema_json, survey_response, stype=stype)

  if stype.qna_map_key is 'initial_assessment':
    sds_key = "SDS - Severity of Dependence Scale"
    raw_answers[sds_key]['sds_score'] = get_total_score(raw_answers[sds_key].values())
  
  return raw_answers, errors
  

def process(data):
  survey_type =  data["meta"]["survey_type"]
  client_id =  data["client_id"]
  date_mod =  data["meta"]["date_modified"].replace(":","") [:17]

  file_name = f"raw_responses/{survey_type}_{client_id}_{date_mod}.json"
  with open(file_name, "w") as wrfile:
    json.dump(data, wrfile)
  #pprint.pprint(data)
  

def insert_data(data, survey_type):
  collection = mydb[survey_type]
  insert(collection, data)



if __name__ == "__main__":
    #survey_id = "271601477"
    #survey_id = "client_registration"
    survey_id = "initial_assessment" #"271604360"

    data , errors = extract(survey_id)    
    #pprint.pprint(data)
    
    process(data)

    #insert_data(data)
    
    #id = "Q5553D234991" 
    #id = "AFTUT23232321"

    #findlatest(id)
    