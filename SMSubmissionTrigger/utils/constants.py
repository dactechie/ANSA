
from collections import namedtuple
from ..config import INITIAL_ASSESSMENT_LOGICAPP_URI, ITSP_LOGICAPP_URI, REGO_LOGICAPP_URI
from ..schema.initial_assessment_schema  import schema as init_assess_schema
from ..schema.client_registration_schema import schema as rego_schema_json


logic_app = namedtuple("LogicApp",["qna_map_key", "uri", "schema"])
                #271601477
survey_type  = {"client_registration": logic_app (qna_map_key="client_registration", uri=REGO_LOGICAPP_URI, schema=rego_schema_json),
                #"271604360"
                "initial_assessment": logic_app (qna_map_key="initial_assessment", uri=INITIAL_ASSESSMENT_LOGICAPP_URI, schema=init_assess_schema),  

                #271695569
               "itsp_review" : logic_app(qna_map_key="itsp_review", uri=ITSP_LOGICAPP_URI, schema=init_assess_schema)               # TODO change the schema ....
              }

