
from ...utils.string_manip import clean

def get_text_qna_open_ended(schema_question, data, trans_dict):
  #q = schema_question['headings'][0]['heading'] 
  if len(data['answers']) == 1:
    return clean(data['answers'][0]['text']) #{q : clean(data['answers'][0]['text']) }

  return  [clean(answer['text']) for answer in data['answers'] ]#{q : [clean(answer['text']) for answer in data['answers'] ] }
