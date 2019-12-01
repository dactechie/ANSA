  # "DEMOGRAPHICS": {
  #   "Date": "11/27/2019",
  #   "team_staff": {
  #     "Your Contact": {
  #       "Team": "Arcadia",
  #       "Team Member": "Tim Ireson"
  #     }
  #   },

def flatten_team_staff(data):
  demog_dict=  data['DEMOGRAPHICS']
  
  team_deets = demog_dict['team_staff']['Your Contact']
  demog_dict['team'] = team_deets['Team']
  demog_dict['staff'] = team_deets['Team Member']
  del demog_dict['team_staff']
  return data

  # "OFFICE USE ONLY:": {
  #   "RISK ASSESSMENTS": {
  #     "risk_suicide": 0,
  #     "risk_dv": 0
  #   },
  #   "CHECKLIST": "ANSA Initial Assessment Booked"
  # },
def flatten_official_use(data):
  off_dict = data['OFFICE USE ONLY']
  data['RISK ASSESSMENTS'] = off_dict['RISK ASSESSMENTS']
  data['CHECKLIST'] = off_dict['CHECKLIST']
  del data['OFFICE USE ONLY']
  return data