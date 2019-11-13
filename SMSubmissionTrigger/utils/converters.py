from .string_manip import clean, kclean
from .slk import generate_slk


def get_storage_kv_dict(arb_dict: dict, fields, values, bit, skip) -> dict:
  results = {}

  for k, v in arb_dict.items():
    vv = v
    if isinstance(vv, dict):
      r = get_storage_kv_dict(vv, fields, values, bit, skip)
      results = {**results, **r}
      continue
    elif isinstance(vv, list):
      vv = get_storage_kv_list(vv, fields, values, bit, skip)
    else:
      vv = kclean(vv)
    #else:
    #  vv = values_table.get(vv,vv)  - doesnt come here

    field = kclean(k)
    field = fields.get(field, field)
    if field in skip:
      continue

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



def get_storage_kv_list(arb_list: list, fields, values, bit, skip) -> list:
  results = []
  for item in arb_list:
    if isinstance(item, dict):
      r = get_storage_kv_dict(item, fields, values, bit, skip)
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


def merge_dicts(data):
  return {k: v for d in data for k, v in d.items()}


# def flatten_hard_vals(data):
#   hardval_keys = ['client_id', 'safety_concern' , 'thoughts_selfharm', 'risk_suicide', 'risk_dv']

def storage_convertor(arb_list, fields, values, bit, skip):
  results = []
  for item in arb_list:
    if isinstance(item, dict):
      r = get_storage_kv_dict(item, fields, values, bit, skip)
      if r:
        results.append(r)
    elif isinstance(item, list):
      r = get_storage_kv_list(item, fields, values, bit, skip)
      results.append(r)

  results = flatten_pages(results)
  results = merge_dicts(results)

  if 'Team.Staff'in results:
    results['team'], results['staff'] = results['Team.Staff']
    del results['Team.Staff']

    results['PDC'], results['method_of_use'] = results['PDC']

    slk = generate_slk(results['Name'], results['dob'], results['gender'])
    results['client_id'] = slk

    del results['Name'], results['dob'], results['gender']

  return results
    

def get_text_by_idlist(idlist, dict_array):
  return (clean(dct['text']) for dct in dict_array if dct['id'] in idlist)


def get_idname_dict(container, items_type, name_field='text'):
  return {item['id']: clean(item[name_field]) for item in container[items_type]}