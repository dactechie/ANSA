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

      stype = survey_type[req_body['name']]  # instead key it off the name of the calling webhook e.g.: ANSA_InitialAssessment_Webhook"
                                
      ## TODO add logic
      # if there was no registration done recently (__or if ep was marked as closed__), 
      # then return error with advice: that have to  register first
      # otherwise get the ClientREgistration ID from Mongo and stick it into the mongo and CDS IntialAssessment object
      
      # Similarly,if there was no InitialAssessment, can't do ITSP review.

      # can_proceed = stype['canproceed_func']()
      # if not can_proceed:
      #   throw CannotProceedError (canProceed)
       
      survey_response = get_survey_responses(sid, rid)
      if 'error' in survey_response: #['error']['http_status_code']         
        raise ResponseRetrievalError(survey_response['error'])

      raw_answers, errors = extract_response(stype.schema, answers_json=survey_response, stype=stype)
      
      if errors:
        logging.error(errors)
      
      # calculate_comparetoprevious_outcomes  (even if only Client Registration  ?)
      if stype.qna_map_key is not 'client_registration' :
        sds_key = "SDS - Severity of Dependence Scale"
        raw_answers[sds_key]['sds_score'] = get_total_score(raw_answers[sds_key].values() )

      # survey_obj (can be of type Rego / Initial/ ITSP)

      # stypeclazz = SurveyClasses [survey_response['custom_variables']['stype']]
      # survey_obj = SurveyObjectFactory.create(stypeclazz ,survey_response)
      # survey_object.extract_raw()         # static functions
      # survey_object.retrieve_process_scores() #method in InitialAsses and ITSP versions 
            
      # collection_ref = mydb[stypeclazz.__name__]
      # dbops.insert(collection_ref, survey_object/SO)
        # inside dbops.insert :
          # SO.Pre_insert():  
            # in the client_reg_SO class nothign to do (client_id is already in the object)
              # add "ep_start_date" ? thats just the client_reg created date
            # in the initial_assessment_SO class add episode_id :
              # get the last (Clients.episode_registrations for this client_id. 


          # inserted_object_id = collection_ref.insert(SO)

          # SO.post_insert  -> 
              # in the client_reg_SO class, post_insert:
                # clients_ref.insert({"episode_registrations"} add -> inserted_objectId)
              # in the initial_assessment_SO class, post_insert:
                # client_registration_ref.update({"initial_assessment"} -> inserted_objectId)
              # in the ITSP_SO class, post_insert:
                # initial_assessment_ref.insert({"ITSP_reviews"} add -> inserted_objectId)



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
             str(e),
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