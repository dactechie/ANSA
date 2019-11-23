from .string_manip import clean, kclean
from .slk import generate_slk


def merge_dicts(data_arr):
  results = {}
  if isinstance(data_arr, dict):
    for d, data in data_arr.items():
      if isinstance(data, list):
        for dd in data:
          if isinstance(dd, dict):
            for kk , vv in dd.items():
              if d in results:
                results[d][kk] = vv
              else:
                results[d] = {kk:vv}

  if not results:
    results = data_arr
  return results


def mapto_storage_kv_dict(arb_dict: dict, fields, values, bit, skip) -> dict:
  results = {}

  for k, v in arb_dict.items():
    vv = v
    if not vv:
      continue
    
    field = kclean(k)
    field = fields.get(field, field)
    if field in skip:
      continue

    if isinstance(vv, dict) :
      # if isinstance(next(iter(vv.values())), dict):
      #   print("cam here ")
      r = mapto_storage_kv_dict(vv, fields, values, bit, skip)
      # if k == 'AOD History':
      #   results = { **results, 'AOD History': merge_dicts(r)  }
      # else:
      results = {**results, field: merge_dicts(r) }
      continue
    elif isinstance(vv, list):
      vv = mapto_storage_kv_list(vv, fields, values, bit, skip)
    else:
      vv = kclean(vv)
    #else:
    #  vv = values_table.get(vv,vv)  - doesnt come here

  
    if field in bit:      
      results[field] = 0 if vv == 'No' else 1
    else:    
      results[field] = vv

  return results


# def get_storage_kv_list_AFTER_IMPLEMENTING_TESTSUITE(arb_list: list) -> list:
#   result_items = [ get_storage_kv_dict(item) 
#                      if isinstance(item, dict)
#                      else values_table.get(item, item)
#                      for item in arb_list ]
#   return [x for x in result_items if x is not None]             



def mapto_storage_kv_list(arb_list: list, fields, values, bit, skip) -> list:
  results = []
  for item in arb_list:
    if isinstance(item, dict):
      # if 'AOD History' in item:
      #   results.append(item)
      #   continue
      r = mapto_storage_kv_dict(item, fields, values, bit, skip)
      if r:
        results.append(r)
    # elif isinstance(item, list):
    #   newlist = get_storage_kv_list(item)
    #   results = results + newlist
    else:
      results.append(values.get(item, item))

  return results


def flatten_pages(pages):
  flattened_pages = []
  
  for page in pages:
    flattened_pages.extend(page)
    
  return flattened_pages


# def flatten_hard_vals(data):
#   hardval_keys = ['client_id', 'safety_concern' , 'thoughts_selfharm', 'risk_suicide', 'risk_dv']
#def storage_demog():
def storage_convertor(arb_list, fields, values, bit, skip):
  results = {}
  for page_title, qna_dict in arb_list.items():
    page_result = None
    if isinstance(qna_dict, dict):
      r = mapto_storage_kv_dict(qna_dict, fields, values, bit, skip)
      if r:
        page_result = r
        #page_result.append(r)
    elif isinstance(qna_dict, list):
      r = mapto_storage_kv_list(qna_dict, fields, values, bit, skip)
      page_result = r #.append(r)
    if page_result:
      results[page_title] = page_result #merge_dicts(page_result) 

  # if 'Team.Staff'in results:
  #   results['team'], results['staff'] = results['Team.Staff']
  #   del results['Team.Staff']

  #   results['PDC'], results['method_of_use'] = results['PDC']

  #   slk = generate_slk(results['Name'], results['dob'], results['gender'])
  #   results['client_id'] = slk

  #   del results['Name'], results['dob'], results['gender']

  return results



def storage_convertor2(arb_list, fields, values, bit, skip):
  results = {}
  for page in arb_list:

    page_title  = list(page)[0]
    page_qna = page[page_title]
    page_result = None#[]

    if isinstance(page_qna, dict):
      r = mapto_storage_kv_dict(page_qna, fields, values, bit, skip)
      if r:
        page_result = r
        #page_result.append(r)
    elif isinstance(page_qna, list):
      r = mapto_storage_kv_list(page_qna, fields, values, bit, skip)
      page_result = r #.append(r)
    
    # for item in page_qna:
    #   if isinstance(item, dict):
    #     r = mapto_storage_kv_dict(item, fields, values, bit, skip)
    #     if r:
    #       page_result.append(r)
    #   elif isinstance(item, list):
    #     r = mapto_storage_kv_list(item, fields, values, bit, skip)
    #     page_result.append(r)



    #page_result = flatten_pages(page_result)
    #page_result = merge_dicts(page_result)

    # if 'Team.Staff'in page_result:
    #   page_result['team'], page_result['staff'] = page_result['Team.Staff']
    #   del page_result['Team.Staff']

    #   page_result['PDC'], page_result['method_of_use'] = page_result['PDC']

    #   slk = generate_slk(page_result['Name'], page_result['dob'], page_result['gender'])
    #   page_result['client_id'] = slk

    #   del page_result['Name'], page_result['dob'], page_result['gender']

    results[page_title] = page_result
    
  return results


# def storage_convertor(arb_list, fields, values, bit, skip):
#   results = []
#   for item in arb_list:
#     if isinstance(item, dict):
#       r = mapto_storage_kv_dict(item, fields, values, bit, skip)
#       if r:
#         results.append(r)
#     elif isinstance(item, list):
#       r = mapto_storage_kv_list(item, fields, values, bit, skip)
#       results.append(r)

#   results = flatten_pages(results)
#   results = merge_dicts(results)

#   if 'Team.Staff'in results:
#     results['team'], results['staff'] = results['Team.Staff']
#     del results['Team.Staff']

#     results['PDC'], results['method_of_use'] = results['PDC']

#     slk = generate_slk(results['Name'], results['dob'], results['gender'])
#     results['client_id'] = slk

#     del results['Name'], results['dob'], results['gender']

#   return results
    

def get_text_by_idlist(idlist, dict_array):
  return (clean(dct['text']) for dct in dict_array if dct['id'] in idlist)


def get_idname_dict(container, items_type, name_field='text'):
  return {item['id']: clean(item[name_field]) for item in container[items_type]}