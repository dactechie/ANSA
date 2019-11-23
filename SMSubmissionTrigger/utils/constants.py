
from collections import namedtuple
from ..schema.initial_assessment_schema  import schema as init_assess_schema
from ..schema.client_registration_schema import schema as rego_schema_json

# TODO : put this in env variables 
INITIAL_ASSESS_URI = "https://prod-20.australiaeast.logic.azure.com:443/workflows/1ad561cb20c5454bb783ac664535d5c0/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=gMMpooW9sGwcsKri_F8NrARl9uKX-AkUsKg-lXnqMcA"

ITSP_LOGIC_APP_URI = "https://prod-26.australiaeast.logic.azure.com:443/workflows/5b6218bd8dc440d28f53e2d1fe6eb91f/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=3WyH8I8K9cXsxNjnXKf6vUNtidqWJUWlRcjvs1C-SVA"

REGO_LOGIC_APP_URI = "https://prod-27.australiaeast.logic.azure.com:443/workflows/49ee573ec4214839a93c30e714d2bf24/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=J_l68JznTNaHpQO36-dcn56h2aldHMZlI7x9RWQ6dRw"

logic_app = namedtuple("LogicApp",["qna_map_key", "uri", "schema"])

survey_type  = {"271875304": logic_app (qna_map_key="client_registration", uri=REGO_LOGIC_APP_URI, schema=rego_schema_json),
                "271604360": logic_app (qna_map_key="initial_assessment", uri=INITIAL_ASSESS_URI, schema=init_assess_schema),  
               "271695569" : logic_app(qna_map_key="itsp_review", uri=ITSP_LOGIC_APP_URI, schema=init_assess_schema)               # TODO change the schema ....
              }

