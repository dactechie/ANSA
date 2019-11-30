from .struct_transformers import flatten_team_staff, flatten_official_use
from .struct_transformers.client_registration import  flatten_substance_use

survey_mappings = {
    
    "struct_transform_funcs": (flatten_team_staff, flatten_substance_use, flatten_official_use),

    "field_table" : {
      "Medicare Number": "medicare",
      "SLK / Client ID": "cid",
      "Do you have a health care card?":"hcc",
      "Did you gamble at all in the past 4 weeks ?": "gamble",

      "Living Arrangements - Who do you live with?": "livar",
      "What is your principal income source?": "pinc",
      "Do you suffer from any allergies?": "allerg",
      "Have you ever been diagnosed with a mental health issue?" : "diagment",
      "Have you ever been hospitalised for a mental health issue?": "hospment",
      
      "Are you accessing support from any other services at the moment?": "othrserv",


      "Your Directions/Pathways Details" : "team_staff",
      'Your Nominated Emergency Contact':'emrgncy',
      #'Country of Birth': 'COB',
      'Date of birth':'dob',
      'Indigenous Status': 'atsi',
      'Client Type': 'clnttyp',
      #'Preferred Language': ''
      'Gender Identity': 'gender',
      'How were you referred to Pathways/Directions?': 'refsrc',
      'Main Substance of Concern' :'PDC',
      'Other substance of concern 1': 'ODC1',
      'Other substance of concern 2': 'ODC2',
      'Other substance of concern 3': 'ODC3',
      'Other substance of concern 4': 'ODC4',
      'Other substance of concern 5': 'ODC5',
      
      'Any other addictive behaviours that concern you?': 'othraddictbhvr',
      'Any indication of suicidal ideation or history?': 'risk_suicide',
      'Any indication of domestic/family violence?': 'risk_dv',
      'Do you have any immediate concerns for the safety and wellbeing of either yourself or others?': 'sftycncrn',
      'Are you experiencing any current thoughts of death/dying or hurting yourself?': 'thghtslfhrm',
      "Discussion about Directions' services - Initial support identified": 'svcsidd',
      'SERVICE GOALS What are your goals regarding alcohol/drug use?': 'svcgoals',
      "Have you ever previously accessed alcohol and/or drug treatment?" : "prevassess",
    },
    "values_table" : {
      'Reduce the harmfulness of my use' : 'ReduceHarmfulness',
      'Not really wanting to change my use at all': 'NotWantChange',
      "Manage the impact of other's alcohol/drug use": 'ManageImpactOthers',
      "Consent to Share Information authority completed" : 'ConsentShareInfo',
    },
    "bit_fields" : ['risk_dv' ,'risk_suicide'],
    "skip_fields" : [ 'Contact Information', 'EmergencyContact']
  }