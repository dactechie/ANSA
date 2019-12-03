
  # "SUBSTANCE USE": {
  #   "pdcmthd": "Ingest",
  #   "AOD History": {
  #     "Alcohol": {
  #       "age1st": "59",
  #       "method": "Smoke",
  #       "Units": "Standard drinks",
  #       "freq": "Irregular Binges",
  #       "perday": "51"
  #     },
  #     "Cannabis": {
  #       "age1st": "13",
  #       "method": "Smoke",
  #       "Units": "Lines",
  #       "freq": "Not Using Anymore",
  #       "perday": "28"
  #     },

def flatten_aod_history(data):
  
  aod_hist_dict = data["SUBSTANCE USE"]["AOD History"]
  data["SUBSTANCE USE"]["AOD History"] = generize_dict(aod_hist_dict, numeric_fields=["age1st", "perday"])
  return data


def flatten_substance_use(data):
  subs_dict = data['SUBSTANCE USE']
  
  pdc_dict = subs_dict['pdcmthd']['Principal Substance of Concern']
  subs_dict["PDC"] = pdc_dict['selection']
  subs_dict['pdc_ndaysconsumed'] = pdc_dict["ndaysconsumed"]
  subs_dict['pdcmthd'] = pdc_dict['method']
  

  subs_dict["odc"] = [{
                      "n" :  k[-1:],
                      "drug" : v['Please select from the dropbox'],
                      "method" : v['method'],
                      "ndaysconsumed": v['ndaysconsumed']
                      }
                      for k , v in subs_dict["odc"].items()]


  inj_dict = subs_dict['inj']['inj']
  subs_dict['injhwlong'] = inj_dict['injhwlong']
  subs_dict['injshare'] = inj_dict['injshare']
  subs_dict['injdays'] = inj_dict['injdays']
  del subs_dict['inj']

  return data

# "EVERYDAY LIVING": {
#     "highedu": "Masters/PHD",
#     "empl": "No - Unemployed",
#     "engag": {
  #       "Paid Work": {
  #         "frequency": "Less than weekly",
  #         "How many days?": "8"
  #       },
  #       "Voluntary Work": {
  #         "frequency": "3 or 4 times per week",
  #         "How many days?": "2"
  #       },
      # "spendtime": {
        # "Drugs & Drinking": {
        #   "Time Spent": "5 - 10 hours per week",
        #   "List your order of priority 1 - 5": "1"
        # },
        # "Hobbies, Sport & Recreation": {
        #   "Time Spent": "40 hours + per week",
        #   "List your order of priority 1 - 5": "5"
        # },

def generize_dict(dct, numeric_fields=None) -> list:
  # if numeric_fields:
  #   for v in dct.values():
  #     for n in numeric_fields:
  #       v[n] = int(v[n])

  result = {}
  for k, v in dct.items():
    for kk, vv in v.items():
      result[f"{k}_{kk}"] = vv

  return result
 # return [ {'_type':k, '_val':v } for k, v in dct.items()]


def flatten_everyday_living(data):
  
  erryday = data["EVERYDAY LIVING"]

  # doing this to make it easier to Parse JSON in the logic app. For each item in the array, 
  # the logic app creates an instance of the entity:ep_everyday_living), which is linked to this particular InitialAssessment
  erryday['engag'] =  generize_dict(erryday['engag'], numeric_fields=['ndays'])
  erryday['spendtime'] = generize_dict(erryday['spendtime'], 
                                  numeric_fields=['p1_5'])

  return data

  # "IMPACT OF SUBSTANCE USE": {
  #   "exprisk": "None of the above",
  #   "addictiveb": {
  #     "Sex": {
  #       "Number of Days": "5"
  #     },
  #     "Internet": {
  #       "Number of Days": "8"
  #     },

def flatten_substance_impact(data):
  impct_addctv = data["IMPACT OF SUBSTANCE USE"]['addictiveb']
  
  addictive = {f"{k}_ndays" : v['Number of Days']
              for k,v in impct_addctv.items() if isinstance(v, dict)}
  
  del data["IMPACT OF SUBSTANCE USE"]['addictiveb']

  data["IMPACT OF SUBSTANCE USE"] = {**data["IMPACT OF SUBSTANCE USE"], **addictive }
  return data
  