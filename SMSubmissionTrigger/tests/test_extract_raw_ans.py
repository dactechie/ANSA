
import json
import pprint
from SMSubmissionTrigger.survey_monkey.response_extractor import extract_response
from SMSubmissionTrigger.utils.constants import survey_type


def test_extract(survey_id):

  stype = survey_type[survey_id]

  #schfname = f"SMSubmissionTrigger/json/{stype}_schema.json"
  
  from SMSubmissionTrigger.schema.client_registration_schema import schema as schema_json
  #schema_json = None
  
  # with open(schfname, "r") as file:
  #   schema_json = json.load(file)
  
  #respfname = f"SMSubmissionTrigger/tests/response_from_gend_initassess.json"
  respfname = f"SMSubmissionTrigger/tests/client_registration_response2.json"
  survey_response = None
  with open(respfname, "r") as file:
    survey_response = json.load(file)
  
  raw_answers = extract_response(schema_json, answers_json=survey_response, stype=stype)
  pprint.pprint(raw_answers)


if __name__ == "__main__":
    survey_id = "271875304"
    # survey_id = "271604360"
    test_extract(survey_id)