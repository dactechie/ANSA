
import json
import logging
import azure.functions as func

from sm_response_extractor import extract_response
from .utils.http_post import forward_results


survey_type  = "client_registration"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
      req_body = req.get_json()
      
      with open(f"json/{survey_type}_schema.json", "r") as file:
        schema_json = json.load(file)
      
      raw_answers = extract_response(schema_json, answers_json=req_body)

      forward_results(raw_answers) # forwards it to a logic app.


    except ValueError as ve:
      logging.error (ve)
      # return func.HttpResponse(
      #        "Unable to get request body JSON",
      #        status_code=400
      #   )
