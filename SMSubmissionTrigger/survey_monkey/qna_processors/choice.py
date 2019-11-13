
from ...utils.string_manip import clean
from ...utils.converters import  get_text_by_idlist


def get_text_qna_single_choice(schema_question, data):
  chosens = get_text_qna_mcq(schema_question, data)
  if chosens:
    return chosens[0]
  return None
 

def get_text_qna_mcq(schema_question, data):
  sch_anss = schema_question['answers']  
  chosens = []
  ans_ch_ids = [answer.get('choice_id') for answer in data['answers']]
  if ans_ch_ids:
    chosens = list(get_text_by_idlist(ans_ch_ids, sch_anss['choices']))

  if sch_anss.get('other'):
    anstext = [clean(answer['text']) for answer in data['answers'] if 'other_id' in answer]
    if anstext:
      chosens.append(anstext[0])

  return chosens