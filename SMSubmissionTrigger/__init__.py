import logging
import azure.functions as func

from .survey_monkey.response_extractor import extract_response
from .utils.http_post import forward_results
from .utils.constants import survey_type
from .utils.scores_answers import get_total_score
from .survey_monkey.sm_api import get_survey_responses
from .ResponseRetrievalError import ResponseRetrievalError
from .db import mydb, operations as dbops


def build_context(data):
  # get survey responses

  # if TSS
  #   construct and fire a request to google sheets -> ADOM
  # else
  #   construct ATOP JSON to be inserted into the excel sheet (which is setup to plot the results)
  pass

def do_sub_tasks(context):
  # try:
  #   context.do_sub_tasks()
  # except:

  pass


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    try:

      req_body = req.get_json()
      logging.info(f"Webhook fired with data: {req_body} \n")
      
      sid = req_body['resources']['survey_id']
      rid = req_body['resources']['respondent_id']

      stype = survey_type[sid]
       
      survey_response = get_survey_responses(sid, rid)
      if 'error' in survey_response: #['error']['http_status_code']         
        raise ResponseRetrievalError({'msg' : "Error while retrieving survey response."})

      raw_answers, errors = extract_response(stype.schema, answers_json=survey_response, stype=stype)
      
      if errors:
        logging.error(errors)
      
      sds_key = "SDS - Severity of Dependence Scale"
      raw_answers[sds_key]['sds_score'] = get_total_score(raw_answers[sds_key].values() )
      
      # collection = mydb[stype.qna_map_key]
      # dbops.insert(collection,raw_answers['client_id'],raw_answers)

      logging.info(raw_answers)
      print(raw_answers)
      
      # if req_body['event_type'] != 'response_completed':
        # handle_incomplete_request
        # lookup DB
        # email the edit URL to staff  
        # raw_answers ['status'] = ''incomplete'
      # else forward to logic app
      forward_results(raw_answers, stype.uri) # forwards it to a logic app.

      
    except ValueError as ve:
      logging.error (ve)
      return func.HttpResponse(
             "Unable to get request body JSON",
             status_code=400
        )
    except ResponseRetrievalError as e:
      logging.error (e)
      return func.HttpResponse(
             "no survey response",
             status_code=400
        )

    
    return func.HttpResponse("Successful",  status_code=200)

  

        # note: it nnever comes here, b/c thois webhook is only fired when "done" is clicked
      # if req_body['event_type'] != 'response_completed':  
      #   # handle_incomplete_request
      #   # lookup DB
      #   # email the edit URL to staff  (with incomplete resuls ?)
      #   logging.error('Survey not completed')
      #   return None


      # {'response_id': '11095161359', 'survey_id': '271875304', 'Country of Birth': 'India', 'Preferred Language': 'English', 
      # 'atsi': 'Torres Strait Islander but not Aboriginal origin', 'client_type': 'Own Alcohol and/or Drug Use', 
      # 'ReferralSource': 'Other community/health care service', 'PDC': 'Benzodiazepines - non-prescribed', 
      # 'ODC1': 'Cannabis', 'ODC2': 'Alcohol', 'other': 'none', 'Goals': ['ReduceHarmfulness', 'NotWantChange', 'ManageImpactOthers'], 
      # 'ServicesIdentified': ['Group participation', 'Althea GP', 'Althea Nurse', 'Althea Psychologist'], 'safety_concern': 'malicious shaming', 
      # 'thoughts_selfharm': 'yes', 'risk_suicide': 1, 'risk_dv': 1, 'CHECKLIST': 'Risk Assessments Completed', 'team': 'Bega Valley',
      #  'staff': 'Tracy Sims', 'method_of_use': 'Inject', 'client_id': 'M22J2190720002'}