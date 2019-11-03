
import json
import logging
import azure.functions as func

from .sm_response_extractor import extract_response
from .utils.http_post import forward_results
from .utils.sm_api import get_survey_responses

survey_type  = {"271875304": "client_registration"}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:

      req_body = req.get_json()
      
      if req_body['event_type'] != 'response_completed':
        logging.error('Survey not completed')
        return None
      
      #submit_datetime = req_body['event_datetime']
      sid = req_body['resources']['survey_id']
      rid = req_body['resources']['respondent_id']

      fname = f"SMSubmissionTrigger/json/{survey_type[sid]}_schema.json"

      with open(fname, "r") as file:
        schema_json = json.load(file)
      
      survey_response = get_survey_responses(sid, rid)
      raw_answers = extract_response(schema_json, answers_json=survey_response)
      
      logging.info(raw_answers)
      print(raw_answers)

      forward_results(raw_answers) # forwards it to a logic app.
      
      # {'response_id': '11095161359', 'survey_id': '271875304', 'Country of Birth': 'India', 'Preferred Language': 'English', 
      # 'atsi': 'Torres Strait Islander but not Aboriginal origin', 'client_type': 'Own Alcohol and/or Drug Use', 
      # 'ReferralSource': 'Other community/health care service', 'PDC': 'Benzodiazepines - non-prescribed', 
      # 'ODC1': 'Cannabis', 'ODC2': 'Alcohol', 'other': 'none', 'Goals': ['ReduceHarmfulness', 'NotWantChange', 'ManageImpactOthers'], 
      # 'ServicesIdentified': ['Group participation', 'Althea GP', 'Althea Nurse', 'Althea Psychologist'], 'safety_concern': 'malicious shaming', 
      # 'thoughts_selfharm': 'yes', 'risk_suicide': 1, 'risk_dv': 1, 'CHECKLIST': 'Risk Assessments Completed', 'team': 'Bega Valley',
      #  'staff': 'Tracy Sims', 'method_of_use': 'Inject', 'client_id': 'M22J2190720002'}
      
    except ValueError as ve:
      logging.error (ve)
      return func.HttpResponse(
             "Unable to get request body JSON",
             status_code=400
        )
    
    return func.HttpResponse("Successful",  status_code=200)
