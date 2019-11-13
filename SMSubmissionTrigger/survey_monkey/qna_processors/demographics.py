

from  SMSubmissionTrigger.utils.converters import  get_idname_dict


def process_demographics(schema, data):

  rows  =  get_idname_dict(schema['answers'], 'rows', 'type')
  results = [ {rows[dans['row_id']]: dans['text']} for dans in data['answers'] ]

  return results
