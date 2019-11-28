#from .struct_transformers import flatten_demographics
  # "SUBSTANCE USE": {
  #   "pdcmthd": {
  #     "Principal Substance of Concern": {   "selection": "Benzodiazapines - prescribed",  "method": "Ingest",  "ndaysconsumed": "23"   }
  #   }, 
  #   "odc": {
  #     "Substances of concern": {   "List up to 5 other substances of concern": "Substances of Concern 3",  "type": "Steroids and other Anabolic Agents",  "ndaysconsumed": "2"   }
  #   }, 
  #   "inj": {
  #     "inj": {   "injhwlong": "More than three months but less than twelve months ago",  "injshare": 1,  "injdays": "19"   }
  #   },

def flatten_substance_use(data):
  subs_dict = data['SUBSTANCE USE']
  
  pdc_dict = subs_dict['pdcmthd']['Principal Substance of Concern']

  subs_dict["PDC"] = pdc_dict['selection']
  subs_dict['pdc_ndaysconsumed'] = pdc_dict["ndaysconsumed"]
  subs_dict['pdcmthd'] = pdc_dict['method']
  
  

  # subs_dict["odc"] = pdc_dict['selection']
  # subs_dict['pdcmthd'] = pdc_dict['method']
  # subs_dict['pdc_ndaysconsumed'] = pdc_dict["ndaysconsumed"]
  #del odc_dict["Substances of concern"]
  inj_dict = subs_dict['inj']['inj']
  subs_dict['injhwlong'] = inj_dict['injhwlong']
  subs_dict['injshare'] = inj_dict['injshare']
  subs_dict['injdays'] = inj_dict['injdays']
  del subs_dict['inj']

  return data