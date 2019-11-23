
from ...utils.string_manip import clean
from ...utils.converters import  get_text_by_idlist


def get_text_qna_single_choice(schema_question, data, trans_dict):
  #q = schema_question['headings'][0]['heading']
  chosens = get_text_qna_mcq(schema_question, data, trans_dict)
  if chosens:
    return chosens[0] #{q: chosens[q][0]}
  return None
 

def get_text_qna_mcq(schema_question, data, trans_dict):
  q = schema_question['headings'][0]['heading']
  sch_anss = schema_question['answers']  
  chosens = []
  ans_ch_ids = [answer.get('choice_id') for answer in data['answers']]
  if ans_ch_ids:
    chosens = list(get_text_by_idlist(ans_ch_ids, sch_anss['choices']))

  if sch_anss.get('other'):
    anstext = [clean(answer['text']) for answer in data['answers'] if 'other_id' in answer]
    if anstext:
      chosens.append(anstext[0])

  return chosens #{q: chosens}