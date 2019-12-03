import pytest
from SMSubmissionTrigger.utils.converters import storage_convertor
from SMSubmissionTrigger.utils.constants import survey_type

processed_aodmatrix =  {'AOD History' :
{
  'Alcohol':[{'Age of First Use': '53'}, {'Method of Use': 'Other'}, {'Units': 'Joints'}, {'How Often?': 'Not Using Anymore'}, {'How much per day?': '24'}],
  'Amphetamine-type substances':[{'Age of First Use': '12'}, {'Method of Use': 'Inject'}, {'Units': 'Lines'}, {'How Often?': 'Irregular Binges'}, {'How much per day?': '26'}],
  'Benzodiazapines - non-prescribed':[{'Age of First Use': '20'}, {'Method of Use': 'Other'}, {'Units': 'Points'}, {'How Often?': 'Irregular Binges'}, {'How much per day?': '43'}],
  'Benzodiazapines - prescribed':[{'Age of First Use': '18'}, {'Method of Use': 'Other'}, {'Units': 'Cigarettes/Darts'}, {'How Often?': 'Irregular Binges'}, {'How much per day?': '60'}],
  'Cannabis':[{'Age of First Use': '34'}, {'Method of Use': 'Ingest'}, {'Units': 'Standard drinks'}, {'How Often?': 'Daily'}, {'How much per day?': '39'}],
  'Cocaine':[{'Age of First Use': '71'}, {'Method of Use': 'Inhale'}, {'Units': 'Dosage (mls)'}, {'How Often?': 'Irregular Binges'}, {'How much per day?': '27'}],
  'Non-prescribed Opioids':[{'Age of First Use': '39'}, {'Method of Use': 'Inhale'}, {'Units': 'Dosage (mgs)'}, {'How Often?': 'Weekly'}, {'How much per day?': '61'}],
  'Other Stimulants/Hallucinogens':[{'Age of First Use': '54'}, {'Method of Use': 'Smoke'}, {'Units': '$$$'}, {'How Often?': 'Daily'}, {'How much per day?': '38'}],
  'Other':[{'Age of First Use': '72'}, {'Method of Use': 'Ingest'}, {'Units': 'Joints'}, {'How Often?': 'Irregular Binges'}, {'How much per day?': '50'}],
  'Precribed Opioid Replacements':[{'Age of First Use': '57'}, {'Method of Use': 'Other'}, {'Units': 'Cones'}, {'How Often?': 'Weekly'}, {'How much per day?': '90'}],
  'Prescribed Opioids':[{'Age of First Use': '74'}, {'Method of Use': 'Smoke'}, {'Units': 'Lines'}, {'How Often?': 'Not Using Anymore'}, {'How much per day?': '19'}],
  'Steroids and other Anabolic Agents':[{'Age of First Use': '29'}, {'Method of Use': 'Inject'}, {'Units': 'Dosage (mgs)'}, {'How Often?': 'Irregular Binges'}, {'How much per day?': '43'}],
  'Tobacco/nicotine':[{'Age of First Use': '45'}, {'Method of Use': 'Other'}, {'Units': 'Dosage (mgs)'}, {'How Often?': 'Weekly'}, {'How much per day?': '49'}]
}
}

'''
  pages.insert(0,[{'survey_type': stype.qna_map_key, 'response_id' : answers_json['id'], 
                   'survey_id' : answers_json['survey_id']}])
  
  mapping_dict = survey_mappings.get(stype.qna_map_key)
  
  res = process_pages(survey_schema, pages, mapping_dict)

  res = storage_convertor(res, field_table, values_table, bit_fields, skip_fields)
'''

# def test_storageconvertor_aodmatrix():
#   # def storage_convertor(arb_list, fields, values, bit, skip):
#   survey_type[]
#   field_table = mapping_dict["field_table"]
#   values_table = mapping_dict["values_table"]
#   bit_fields = mapping_dict["bit_fields"]
#   skip_fields = mapping_dict["skip_fields"]
  
#   pages = 
#   storage_convertor(processed_aodmatrix)