#import sys
#import re

from SMSubmissionTrigger.utils.string_manip import clean
from SMSubmissionTrigger.utils.converters import storage_convertor
from .qna_processors import qtype_handlers
from ..qna_mappings import surveys

# id_types = ['row_id', 'col_id', 'choice_id']
# id_types_list_map = {'row_id':'rows' , 'col_id': 'cols', 'choice_id': 'choices'}

# meta data to store 
'''
"href": "https://api.surveymonkey.net/v3/surveys/271026860/responses/11075389573",
 "date_created": "2019-10-18T00:34:54+00:00", 
 "date_modified": "2019-10-18T11:22:40+00:00", "response_status": "completed", 
 "collector_id": "247867892", 
'''

'''
  survey_schema : json object
'''
def extract_response(survey_schema, answers_json, stype=None):
  pages = answers_json['pages']

  # TODO insert datetime of the submission
  pages.insert(0,[{'response_id' : answers_json['id'], 'survey_id' : answers_json['survey_id']}])
  
  res = process_pages(survey_schema, pages)

  survey_dict = surveys.get(stype)

  field_table = survey_dict["field_table"]
  values_table = survey_dict["values_table"]
  bit_fields = survey_dict["bit_fields"]
  skip_fields = survey_dict["skip_fields"]


  res = storage_convertor(res, field_table, values_table, bit_fields, skip_fields)

  return res



def process_question(schema_question, question):
  question_text = clean(schema_question['headings'][0]['heading'])
  results = None
  
  txt_replace_fn = qtype_handlers.get(schema_question['family'])
  if txt_replace_fn:
    results = {question_text : txt_replace_fn(schema_question, question)}
    #print (results)
  else:
    print(f"\n\n...........family : {schema_question['family']}\n\n")
  
  return results



def schema_for_question_id(schema_questions, response_qid):
  return next(sq for sq in schema_questions if sq['id'] == response_qid)


def process_page(sch_qs, response_qs):

  q_schemas__respq = [(schema_for_question_id(sch_qs, resp_q['id']), resp_q) 
                        for resp_q in response_qs]

  # some questions may not have been answered, filter them out
  q_schemas__respq = filter(lambda qs: qs[0] != None, q_schemas__respq)

  return [process_question(q_schema, resp_q)
            for q_schema, resp_q in q_schemas__respq]
 
    

def process_pages(qna_id_defs, pages):

  results = [pages.pop(0)] # meta information like date_Created, survey_id , response_id 

  for counter, page in enumerate(pages):
    res = process_page(qna_id_defs['pages'][counter]['questions'],
                       page['questions'])
    results.append(res)

  return results





#def get_idname_dict(container, items_type, name_field='text'):
#  return {item['id']: clean(item[name_field]) for item in container[items_type]}
#
