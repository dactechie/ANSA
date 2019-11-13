
from SMSubmissionTrigger.utils.string_manip import clean

def get_text_qna_open_ended(schema_question, data):
  if len(data['answers']) == 1:
    return clean(data['answers'][0]['text'])

  return  [clean(answer['text']) for answer in data['answers'] ]
