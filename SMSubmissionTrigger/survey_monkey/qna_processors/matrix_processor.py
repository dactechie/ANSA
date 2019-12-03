from ...utils.converters import (storage_convertor,
                                          get_text_by_idlist, get_idname_dict)
from ...utils.string_manip import clean


def build_text_matrix_with_cols (schema):

  rows = get_idname_dict(schema, 'rows')
  cols = get_idname_dict(schema, 'cols')
  
  cols_choices = { col['id']: get_idname_dict(col, 'choices')
                   for col in schema['cols']  }
  return rows, cols, cols_choices



# def process_matrix_with_cols_AFTERIMPLEMENTING_TESTSUITE(matrix_schema, data):
#   rows, cols, cols_choices = build_text_matrix_with_cols (matrix_schema['answers'])
  
#   results1, data_answers = handle_otherids(data['answers']) #data_answers now has no other_ids
#   results2, data_answers = handle_nocols(data_answers, rows, cols, cols_choices ) # data
#   results3 = handle_col_choices(data_answers)
#   return {**results1, **results2, **results3}


def process_matrix_with_cols(matrix_schema, data, trans_dict):
  rows, cols, cols_choices = build_text_matrix_with_cols (matrix_schema['answers'])
  results =  {} #{'rows': rows.values(), 'cols': cols.values()}

  for answer in data['answers']:
    row_id = answer.get('row_id')
    if not row_id and answer.get('other_id'):
      results['other'] = answer['text']
      continue
    
    rtext = rows[row_id]
    ans_col_id = answer['col_id']
    ans_choice_id = answer['choice_id']

    ctext = cols[ ans_col_id ]
    col_choices = cols_choices[ ans_col_id ]
    if not ctext:
      results[rtext] = clean(col_choices[ans_choice_id])  # not a list unlike below ..append and = []
      continue

    #ans = clean(col_choices[ans_choice_id]) 
    ans = { clean(ctext) : clean(col_choices[ans_choice_id]) }
    
    if results.get(rtext):
      results[rtext].append(ans)
    else:
      results[rtext]= [ans]
       
  rr = {}
  for k, v in results.items():
      if len(v) == 1:
        rr[k] = v[0]
      else:
        rr[k] = v
        
  return rr


def build_text_matrix_no_cols (schema): # answers schema
  
  rows = get_idname_dict(schema, 'rows')
  choices = get_idname_dict(schema, 'choices')

  return rows, choices


# def process_matrix_with_NO_cols_AFTERIMPLEMENTING_TESTSUITE(matrix_schema, data):
#   rows, choices = build_text_matrix_no_cols (matrix_schema['answers'])
  
#   results1, data_answers = handle_otherids(data['answers']) #data_answers now has no other_ids

#   ...

# TODO : this continues after assigning result.. shouldn't it either append to a list of results or just return ?
# if there are selections from (1) a list of choices  AND (2) "other" then we need both answers

def process_matrix_no_cols(matrix_schema, data, trans_dict):
  rows, choices = build_text_matrix_no_cols (matrix_schema['answers'])
  results = None
  if len(data['answers']) > 1:
    print(f"more than one answer ..................................{data['answers']}.................................................. ?")
  for answer in data['answers']:
    #{'other_id': '2413710781', 'text': 'sexting'}
    row_id = answer.get('row_id')
    if not row_id and answer.get('other_id'):
      results = f"other_{answer['text']}"
      #results.append({'other' : answer['text']})
      continue

    rtext = rows[answer['row_id']]
    ans_choice_id = answer['choice_id']
    if not rtext:
      results = choices [ans_choice_id] 
    else:
      print(f".....................................{rtext}............................................... ?")
      #results.append ({rtext : choices [ans_choice_id]})
      #print("SHOULD NOT COME  HERE : process_matrix_no_cols")
      #sys.exit()

  return results


def get_text_qna_matrix(matrix_schema, data, trans_dict):
  if matrix_schema['id'] != data['id']:

    print("Error - question IDs don't match. \n\t")
    return None
  #q = matrix_schema['headings'][0]['heading'] 
  if matrix_schema['answers'].get('cols'):
    return process_matrix_with_cols (matrix_schema, data, trans_dict)#{q: process_matrix_with_cols (matrix_schema, data, trans_dict)}
  else:
    return process_matrix_no_cols (matrix_schema, data, trans_dict)#{q:process_matrix_no_cols (matrix_schema, data, trans_dict)}

