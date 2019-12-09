import json
import pytest
from pprint import pprint
from SMSubmissionTrigger.survey_monkey import response_extractor
from SMSubmissionTrigger.schema.initial_assessment_schema import schema as question_schema
from SMSubmissionTrigger.schema.qna_mapping.initial_assessment import survey_mappings

# @fixture()
# def sfs():
#   pass

def get_question(question_schema, qid):
  for p in question_schema['pages']:
    for q in p['questions']:
      if q['id'] == qid:
        return q
  return None


def test_process_question_aodhistory_matrix():
  response_fname = f"SMSubmissionTrigger/survey_monkey/tests/aodmatrix_answers.json"
  
  survey_response = None
  with open(response_fname, "r") as file:
    survey_response = json.load(file)

  question  = get_question(question_schema, survey_response['id'])
  
  output = response_extractor.process_ans_for_question(
                              question, survey_response, survey_mappings)

  #{ 'AOD History' : 
  expected =  {'Alcohol': [{'Age of First Use': '53'},
                         {'Method of Use': 'Other'},
                         {'Units': 'Joints'},
                         {'How Often?': 'Not Using Anymore'},
                         {'How much per day?': '24'}],
             'Amphetamine-type substances (eg. ice, methamphetamine)': [{'Age of First Use': '12'},
                                                                        {'Method of Use': 'Inject'},
                                                                        {'Units': 'Lines'},
                                                                        {'How Often?': 'Irregular '
                                                                                       'Binges'},
                                                                        {'How much per day?': '26'}],
             'Benzodiazapines - non-prescribed': [{'Age of First Use': '20'},
                                                  {'Method of Use': 'Other'},
                                                  {'Units': 'Points'},
                                                  {'How Often?': 'Irregular Binges'},
                                                  {'How much per day?': '43'}],
             'Benzodiazapines - prescribed': [{'Age of First Use': '18'},
                                              {'Method of Use': 'Other'},
                                              {'Units': 'Cigarettes/Darts'},
                                              {'How Often?': 'Irregular Binges'},
                                              {'How much per day?': '60'}],
             'Cannabis': [{'Age of First Use': '34'},
                          {'Method of Use': 'Ingest'},
                          {'Units': 'Standard drinks'},
                          {'How Often?': 'Daily'},
                          {'How much per day?': '39'}],
             'Cocaine': [{'Age of First Use': '71'},
                         {'Method of Use': 'Inhale'},
                         {'Units': 'Dosage (mls)'},
                         {'How Often?': 'Irregular Binges'},
                         {'How much per day?': '27'}],
             'Non-prescribed Opioids (eg. heroin)': [{'Age of First Use': '39'},
                                                     {'Method of Use': 'Inhale'},
                                                     {'Units': 'Dosage (mgs)'},
                                                     {'How Often?': 'Weekly'},
                                                     {'How much per day?': '61'}],
             'Other': [{'Age of First Use': '72'},
                       {'Method of Use': 'Ingest'},
                       {'Units': 'Joints'},
                       {'How Often?': 'Irregular Binges'},
                       {'How much per day?': '50'}],
             'Other Stimulants/Hallucinogens (eg. MDMA, Ecstacy)': [{'Age of First Use': '54'},
                                                                    {'Method of Use': 'Smoke'},
                                                                    {'Units': '$$$'},
                                                                    {'How Often?': 'Daily'},
                                                                    {'How much per day?': '38'}],
             'Prescribed Opioid Replacements (methadone/buprenorphine)': [{'Age of First Use': '57'},
                                                                          {'Method of Use': 'Other'},
                                                                          {'Units': 'Cones'},
                                                                          {'How Often?': 'Weekly'},
                                                                          {'How much per day?': '90'}],
             'Prescribed Opioids (eg. oxycodone, tramadol, fentanyl)': [{'Age of First Use': '74'},
                                                                        {'Method of Use': 'Smoke'},
                                                                        {'Units': 'Lines'},
                                                                        {'How Often?': 'Not '
                                                                                       'Using '
                                                                                       'Anymore'},
                                                                        {'How much per day?': '19'}],
             'Steroids and other Anabolic Agents': [{'Age of First Use': '29'},
                                                    {'Method of Use': 'Inject'},
                                                    {'Units': 'Dosage (mgs)'},
                                                    {'How Often?': 'Irregular Binges'},
                                                    {'How much per day?': '43'}],
             'Tobacco/nicotine': [{'Age of First Use': '45'},
                                  {'Method of Use': 'Other'},
                                  {'Units': 'Dosage (mgs)'},
                                  {'How Often?': 'Weekly'},
                                  {'How much per day?': '49'}]
                      }
  #}
  assert expected == output
