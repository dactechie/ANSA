
import json
import pprint
from SMSubmissionTrigger.survey_monkey.response_extractor import extract_response
from SMSubmissionTrigger.utils.constants import survey_type
#from SMSubmissionTrigger.db import mydb

# def write_to_db(data):
#    mycol = mydb["initial_assessment"]
#    x = mycol.insert_one(data)

#    print(x)



def test_extract(survey_id):

  stype = survey_type[survey_id]

  #schfname = f"SMSubmissionTrigger/json/{stype}_schema.json"
  if stype.qna_map_key is 'initial_assessment' :
    from SMSubmissionTrigger.schema.initial_assessment_schema import schema as schema_json
    #from SMSubmissionTrigger.schema.matrix_aod_history import schema as schema_json
    #from SMSubmissionTrigger.schema.text_matrix_rating_other import schema as schema_json
    
  else:
    from SMSubmissionTrigger.schema.client_registration_schema import schema as schema_json
    
  #schema_json = None
  
  # with open(schfname, "r") as file:
  #   schema_json = json.load(file)
  
  respfname = f"SMSubmissionTrigger/tests/initial_assessment_generated_response2.json"
  #respfname = f"SMSubmissionTrigger/tests/matrix_rating_other.json"
  #respfname = f"SMSubmissionTrigger/tests/client_registration_response2.json"
  survey_response = None
  with open(respfname, "r") as file:
    survey_response = json.load(file)
  
  raw_answers = extract_response(schema_json, answers_json=survey_response, stype=stype)
  # with open("b.json", "w") as wrfile:
  #   json.dump(raw_answers, wrfile)
  pprint.pprint(raw_answers)
  #write_to_db(raw_answers)


if __name__ == "__main__":
    #survey_id = "271875304"
    survey_id = "271604360"
    test_extract(survey_id)