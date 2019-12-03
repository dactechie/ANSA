#import sys
#import re

from ..utils.string_manip import clean
from ..utils.converters import storage_convertor
from .qna_processors import qtype_handlers
#from ..qna_mappings import survey_mappings


# id_types = ['row_id', 'col_id', 'choice_id']
# id_types_list_map = {'row_id':'rows' , 'col_id': 'cols', 'choice_id': 'choices'}

def data_from_fieldpath(data, field_path:str):
  k, v = field_path.split('.')
  return str.strip(data[k][v])


def is_incomplete_response(data, incomplete_if_empty):
  try:
    return any(False if data_from_fieldpath(data,field) else True 
              for field in incomplete_if_empty )
  except KeyError:
    return True


# meta data to store 
def extract_meta(data, answers_json, survey_type, incomplete_if_empty: tuple):

  staff_name = data['DEMOGRAPHICS']['staff']
  staff_name =  staff_name.replace(" ",".",1).strip()
  staff_email = f"{staff_name}@directionshealth.com"

  is_incomplete = is_incomplete_response(data, incomplete_if_empty)
  meta_dict = { 'meta':
                {'survey_type': survey_type, 'response_id' : answers_json['id'], 
                'survey_id' : answers_json['survey_id'], 
                'date_created': answers_json['date_created'], 'date_modified': answers_json['date_modified'],
                'staff_email': staff_email, 
                'is_incomplete': is_incomplete}
              }

  if is_incomplete:
    meta_dict['edit_url']= answers_json['edit_url']

  return meta_dict

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
  errors = []
  pages = answers_json['pages']
  
  if stype.qna_map_key is 'client_registration':
    from ..schema.qna_mapping.client_registration import survey_mappings as mapping_dict
  else:
    from ..schema.qna_mapping.initial_assessment import survey_mappings as mapping_dict

  res = ids_to_raw(survey_schema, pages, mapping_dict)
  
  # field_table = mapping_dict["field_table"]
  # values_table = mapping_dict["values_table"]
  # bit_fields = mapping_dict["bit_fields"]
  # skip_fields = mapping_dict["skip_fields"]

  res = storage_convertor(res, mapping_dict)
    
  for func in mapping_dict['struct_transform_funcs']:
    res = func(res)

  if 'custom_variables' in answers_json and 'client_id' in answers_json['custom_variables']:
    res['client_id'] = answers_json['custom_variables'].get('client_id')
  elif 'client_id' in res['DEMOGRAPHICS']:
    res['client_id'] = res['DEMOGRAPHICS']['client_id']
  else:
    errors.append("MissingClientID")
  
  # else:
  #   res['client_id'] = res['DEMOGRAPHICS']['client_id'] # it was typed into the form?  -> remove the need for this, the URL would always insert it.
  
  meta = extract_meta(res, answers_json, stype.qna_map_key, mapping_dict['incomplete_if_empty'])
  #staff_name = res['DEMOGRAPHICS'].get('team_staff').get("Your Contact").get("Team Member")
  res = {**res, **meta}

  #res['errors'] = ",".join(errors)
  return res, errors



def process_question(schema_question, question, trans_dict):
  
  results = None
  
  txt_replace_fn = qtype_handlers.get(schema_question['family'])
  if txt_replace_fn:
    results =  txt_replace_fn(schema_question, question, trans_dict)
    #print (results)
  else:
    print(f"\n\n...........family : {schema_question['family']}\n\n")
  
  return results



def schema_for_question_id(schema_questions, response_qid):
  return next(sq for sq in schema_questions if sq['id'] == response_qid)


def process_page(sch_qs, response_qs, trans_dict):

  q_schemas__respq = [(schema_for_question_id(sch_qs, resp_q['id']), resp_q) 
                        for resp_q in response_qs]

  # some questions may not have been answered, filter them out
  q_schemas__respq = filter(lambda qs: qs[0] != None, q_schemas__respq)

  qna = {}
  for q_schema, resp_q in q_schemas__respq:
    question_text = clean(q_schema['headings'][0]['heading'])
    
    #qna.setdefault(question_text, process_question(q_schema, resp_q, trans_dict))
    if qna.get(question_text):
      qna[question_text].append(process_question(q_schema, resp_q, trans_dict))
    else:
      qna[question_text] = process_question(q_schema, resp_q, trans_dict)

  return qna
 
    

def ids_to_raw(qna_id_defs, pages, trans_dict):

  
  results = {} # {'meta' : pages.pop(0)} # meta information like date_Created, survey_id , response_id 

  for counter, page in enumerate(pages):
    res = process_page(qna_id_defs['pages'][counter]['questions'],
                       page['questions'], trans_dict)
    page_title = qna_id_defs['pages'][counter]['title']
    results[page_title] = res
    #results.append(res)

  return results





#def get_idname_dict(container, items_type, name_field='text'):
#  return {item['id']: clean(item[name_field]) for item in container[items_type]}
#
