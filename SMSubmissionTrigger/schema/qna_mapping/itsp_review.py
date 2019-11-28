from .initial_assessment import survey_mappings as ia_map

def without_keys(src_dict, not_allowed_keys):
  return {x: src_dict[x] for x in src_dict if x not in not_allowed_keys}

not_in_itsp_review = {"Have you ever previously accessed alcohol and/or drug treatment?",
                      "What is your highest level of education?",
                      "What is your principal income source?",
                      "Do you have a GP or medical centre that you regularly attend?",
                      "Have you ever been diagnosed with a mental health issue?",
                      "Have you served a custodial sentence in the past?"
                     }



itsp_review = { **ia_map['values_table'], 'bit_fields' : ia_map['bit_fields']}

itsp_review['field_table'] = without_keys(
                                ia_map['field_table'],
                                not_in_itsp_review)

ia_map['itsp_review'] = itsp_review

survey_mappings = ia_map


# from pprint import pprint

# def without_keys(src_dict, not_allowed_keys):
#   return {x: src_dict[x] for x in src_dict if x not in not_allowed_keys}

# not_in_itsp_review = {"Have you ever previously accessed alcohol and / or drug treatment?",
#                       "What is your highest level of education?",
#                       "What is your principal income source?",
#                       "Do you have a GP or medical centre that you regularly attend?",
#                       "Have you ever been diagnosed with a mental health issue?",
#                       "Have you served a custodial sentence in the past?"
#                      }

# ini_as = survey_mappings['initial_assessment']

# itsp_review = { **ini_as['values_table'], 'bit_fields' : ini_as['bit_fields']}

# itsp_review['field_table'] = without_keys(
#                                 ini_as['field_table'],
#                                 not_in_itsp_review)

# survey_mappings['itsp_review'] = itsp_review

# pprint(itsp_review)