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


