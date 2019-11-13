from .matrix_processor import get_text_qna_matrix
from .choice import get_text_qna_mcq, get_text_qna_single_choice
from .open_ended import get_text_qna_open_ended
from .demographics import process_demographics


qtype_handlers = {
  'matrix' : get_text_qna_matrix,
  'multiple_choice' : get_text_qna_mcq,
  'single_choice': get_text_qna_single_choice,
  'open_ended': get_text_qna_open_ended,
  'datetime' : get_text_qna_open_ended,
  'demographic' : process_demographics
}
