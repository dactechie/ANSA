from .string_manip import clean, kclean
from .slk import generate_slk


'''
  For heaven's sake, find a better soluton than this !!
'''
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


def get_good_fieldvals(arb_dict, fields, skip):

  for k, val in arb_dict.items():  
    if not val:
      continue
    
    field = kclean(k)
    field = fields.get(field, field)
    if field in skip:
      continue

    yield field, val


def mapto_storage_kv_dict(arb_dict: dict, fields, values, bit, skip) -> dict:
  results = {}

  for field, val in get_good_fieldvals(arb_dict, fields, skip):
    vv = val

    if isinstance(vv, dict) :
      r = mapto_storage_kv_dict(vv, fields, values, bit, skip)
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
      r = mapto_storage_kv_dict(item, fields, values, bit, skip)
      if r:
        results.append(r)
    else:
      results.append(values.get(item, item))

  return results


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

  return results


def get_text_by_idlist(idlist, dict_array):
  return (clean(dct['text']) for dct in dict_array if dct['id'] in idlist)


def get_idname_dict(container, items_type, name_field='text'):
  return {item['id']: clean(item[name_field]) for item in container[items_type]}