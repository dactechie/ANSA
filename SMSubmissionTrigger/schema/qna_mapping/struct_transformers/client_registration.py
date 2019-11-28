

  # "DEMOGRAPHICS": {
  #   "Date": "11/27/2019",
  #   "team_staff": {
  #     "Your Contact": {
  #       "Team": "Arcadia",
  #       "Team Member": "Tim Ireson"
  #     }
  #   },

def flatten_demographics(data):
  demog_dict=  data['DEMOGRAPHICS']
  
  team_deets = demog_dict['team_staff']['Your Contact']
  demog_dict['team'] = team_deets['Team']
  demog_dict['staff'] = team_deets['Team Member']
  del demog_dict['team_staff']
  return data
'''
def flatten_demographics(data):
  demog_dict=  data['DEMOGRAPHICS']
  
  team_deets = demog_dict['Your Directions/Pathways Details']['Your Contact']
  demog_dict['team'] = team_deets[0]['Team']
  demog_dict['staff'] = team_deets[1]['Team Member']
  del demog_dict['Your Directions/Pathways Details']
  return data

'''

  # "SUBSTANCE USE": {
  #   "Principal Substance of Concern": {
  #     "PDC": {
  #       "Please select from the dropbox": "Prescribed Opioid replacements",
  #       "Method of use Ingest/Smoke/Inject/Sniff/Inhale/Other": "Other"
  #     }
  #   },
  #   "Other Substances of Concern": {
  #         "ODC1": {
  #           "Please select from the dropbox": "Cannabis"
  #         },
  #         "ODC2": {
  #           "Please select from the dropbox": "Non-prescribed opioids"
  #         },

def flatten_substance_use(data):
  subs_dict = data['SUBSTANCE USE']
  pdc_dict = subs_dict['Principal Substance of Concern']['PDC']
  pdc = pdc_dict["Please select from the dropbox"]
  method = pdc_dict['Method of use Ingest/Smoke/Inject/Sniff/Inhale/Other']


  subs_dict['PDC'] = pdc
  subs_dict['pdcmthd'] = method
  del subs_dict['Principal Substance of Concern']


  other = subs_dict["Other Substances of Concern"]
  for odc_key, odc_dict in other.items():
    subs_dict[odc_key] = odc_dict["Please select from the dropbox"]
  del subs_dict["Other Substances of Concern"]


  # "SUBSTANCE USE": {
  #   "othraddictbhvr": {
  #     "Other Addictive Behaviours": "Porn"
  #   },
  #   "gamble": {
  #     "Number of Days": {
  #       "Days": "2"
  #     }
  #   },
  
  subs_dict['othraddictbhvr'] = subs_dict['othraddictbhvr']["Other Addictive Behaviours"]
  subs_dict['gamble_days'] = subs_dict['gamble']['Number of Days']['Days']

  
  del subs_dict['gamble']
  return data


  # "OFFICE USE ONLY:": {
  #   "RISK ASSESSMENTS": {
  #     "risk_suicide": 0,
  #     "risk_dv": 0
  #   },
  #   "CHECKLIST": "ANSA Initial Assessment Booked"
  # },
def flatten_official_use(data):
  off_dict = data['OFFICE USE ONLY:']
  data['RISK ASSESSMENTS'] = off_dict['RISK ASSESSMENTS']
  data['CHECKLIST'] = off_dict['CHECKLIST']
  del data['OFFICE USE ONLY:']
  return data