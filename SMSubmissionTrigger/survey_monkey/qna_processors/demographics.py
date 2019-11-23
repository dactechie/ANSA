

from  ...utils.converters import  get_idname_dict


def process_demographics(schema, data, trans_dict):
  #q = schema['headings'][0]['heading']
  rows  =  get_idname_dict(schema['answers'], 'rows', 'type')
  results = [ {rows[dans['row_id']]: dans['text']} for dans in data['answers'] ]

  return results #{q: results}
