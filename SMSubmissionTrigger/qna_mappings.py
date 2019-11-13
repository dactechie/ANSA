
survey_mappings = {
  "client_registration" : {

    "field_table" : {
      'Your Contact' : 'Team.Staff',
      'Your Nominated Emergency Contact':'EmergencyContact',
      #'Country of Birth': 'COB',
      'Date of birth':'dob',
      'Indigenous Status': 'atsi',
      'Client Type': 'client_type',
      #'Preferred Language': ''
      'Gender Identity': 'gender',
      'How were you referred to Pathways/Directions?': 'ReferralSource',
      'Main Substance of Concern' :'PDC',
      'Other substance of concern 1': 'ODC1',
      'Other substance of concern 2': 'ODC2',
      'Other substance of concern 3': 'ODC3',
      'Other substance of concern 4': 'ODC4',
      'Other substance of concern 5': 'ODC5',
      'Any other addictive behaviours that concern you?': 'OtherAddictiveBehaviour',
      'Any indication of suicidal ideation or history?': 'risk_suicide',
      'Any indication of domestic/family violence?': 'risk_dv',
      'Do you have any immediate concerns for the safety and wellbeing of either yourself or others?': 'safety_concern',
      'Are you experiencing any current thoughts of death/dying or hurting yourself?': 'thoughts_selfharm',
      "Discussion about Directions' services Initial support identified": 'ServicesIdentified',
      'SERVICE GOALS What are your goals regarding alcohol/drug use?': 'Goals'
    },
    "values_table" : {
      'Reduce the harmfulness of my use' : 'ReduceHarmfulness',
      'Not really wanting to change my use at all': 'NotWantChange',
      "Manage the impact of other's alcohol/drug use": 'ManageImpactOthers'    
    },
    "bit_fields" : ['risk_dv' ,'risk_suicide'],
    "skip_fields" : [ 'Contact Information', 'EmergencyContact']
  },


  "ITSP" :{
    
    "field_table": {
      "Assessment Date" : "surv_date",
      # "Your Directions / Pathways Details:"
      "SLK / Client ID": "cid",
      "Principal Substance of Concern and Method of Use(if changed since registration)": "pdc",
      "Other substances of concern(if changed since registration)" :"odc",
      "Injecting Drug Status": "inj",
      "How long since you last injected?": "injhwlong",
      "Shared Any Equipment?<br>(incl. needles, syringes, waters, spoons, filters)": "injshare",
      "Number of Injecting Days in the last 4 weeks?": "injdays",

      # "AOD History"
      "Do you ever think that your drug/alcohol use is out of control?": "outctrl",
      "Does the prospect of missing a session fix make you very anxious or nervous?" : "missanx",
      "How much do you worry about your use of drugs/alcohol?": "worry",
      "Do you wish you could stop?" : "stop",
      "How difficult would you find it to stop or go without your substance of concern?" : "diffstop",
      "AOD Harms/Risks In the last 4 weeks, have you experienced any of the following risks?" : "exprisk",
      "Have you ever previously accessed alcohol and/or drug treatment?" : "prevassess",
      "Did you gamble at all in the last 4 weeks (28 days)?": "gamble",
      "Did you engage in any other addictive behaviours in the last 4 weeks?": "addictiveb",
      "# Impact on Daily Living During the last 4 weeks, how often has your substance use  impacted on your work or other daily living activities ?":"impactliving",
      "SUMMARY OF SUBSTANCE USE PRESENTING ISSUES Notes for ITSP":"ni_sum_pres_issues",
      "SUBSTANCE USE GOALS Notes for ITSP": "ni_goals",
      "Usual Accommodation":  "usuaccom",
      "Living Arrangements - Who do you live with?": "livar",
      # "Your Current Housing"
      "# Housing Stability In the past 4 weeks, have you had any difficulties with housing or finding somewhere stable to live?": "diffhouse",
      "Physical Safety Do you feel safe where you live?" : "physafety",
      "Do you have any concerns for the safety and wellbeing of either yourself or others?": "safety_concern",
      "SUMMARY OF HOUSING & SAFETY PRESENTING ISSUES Notes for ITSP": "ni_hou_saft",
      "HOUSING & SAFETY GOALS Notes for ITSP": "ni_goals_housaft",
      "What is your highest level of education?" : "highedu",
      "Are you currently employed?": "empl",
      "What is your principal income source?": "pinc",
      "In the last 4 weeks, how often have you engaged in any of the following?": "engag",
      "Study - college, school or vocational education": "eng_edu",
      "How much time per week do you spend on....?": "spendtime",
      "SUMMARY OF EVERYDAY LIVING PRESENTING ISSUES Notes for ITSP" : "ni_livissu",
      "EVERYDAY LIVING GOALS Notes for ITSP": "ni_goals_livissu",
      "How has your physical health been, in the last 4 weeks?": "phyheal",
      "#How often has your health caused problems in your daily life?": "healcauseprob",
      "Do you have a GP or medical centre that you regularly attend?": "regumedic",
      "In the past 4 weeks have you been in hospital or needed to call an ambulance?" : "ambu",
      "Are you currently taking any medications?": "medications",
      "Do you suffer from any allergies?": "allerg",
      # "Health Checklist"
      "SUMMARY OF PHYSICAL HEALTH & WELLBEING PRESENTING ISSUES Notes for ITSP": "ni_sum_welb",
      "PHYSICAL HEALTH & WELLBEING GOALS: Notes for ITSP":"ni_goals_welb",
      "How has your psychological/mental health been? Do you have moods, fears, emotions or other thoughts that concern you?":"mentrate",
      "Sleep Do you have any sleep issues? Check all that apply": "sleep",
      "# How often does your mental health create problems in your daily life?": "mentcauseprob",
      "Have you ever been diagnosed with a mental health issue?" : "diagment",
      "Have you have ever been hospitalised for a mental health issue?" : "hospment",
      "Have you experienced any thoughts of death/dying or of hurting yourself?": "thoughtsofhurt",
      
      
      "Mental Health Risk Issues": "risk_ment_issues",
      "Any indication of mental health risks?": "risk_ment",

      "SUMMARY OFMENTAL HEALTH & WELLBEING PRESENTING ISSUES Notes for ITSP": "ni_sum_ment",
      "MENTAL HEALTH & WELLBEING GOALS Notes for ITSP": "ni_goals_ment",
      "Social/Community Connections Do you have family/social connections who are positive and supportive? Are you involved in your community?": "socommconn",
      "# How often does your substance use lead to problems or arguments with family members or friends?": "famprob",
      "Has anyone been violent or abusive towards you?": "violtoyou",
      "Have you used violence or been abusive towards anyone?": "violbyyou",
      "Parenting/Caregiving Do you have parenting/caregiving responsibilities? Are you the primary caregiver for, or living with, any children?" : "caregiving",
      
      "Any indication of domestic/family violence?": "risk_dv",
      #"Any indication of suicidal ideation or history?": "risk_suicide",
      "Any indication of suicidal ideation?": "risk_suicide",
      "Are there any child protection concerns? Have either FaCS  or OCYFS  been involved with your family?": "childprot",
      "RELATIONSHIPS, PARENTING & SOCIAL WELLBEING - PRESENTING ISSUES Notes for ITSP": "ni_rel",
      "RELATIONSHIPS, PARENTING & SOCIAL WELLBEING - GOALS Notes for ITSP": "ni_goals_rel",
      "Have you served a custodial sentence in the past?": "custod",
      "Legal Have you been arrested in the last 4 weeks?" : "arrest",
      "# In the last 4 weeks, how often have you been involved in any illegal activities? ?": "illegal",
      "Are you currently subject to court orders or have any charges pending?": "crtorder",
      "Do you need help with a Work Development Order to pay off any outstanding fines?": "wrkdevorder",
      "SUMMARY OF LEGAL PRESENTING ISSUES Notes for ITSP": "ni_legal",
      "LEGAL GOALS Notes for ITSP": "ni_goals_legal",
      "Optimism/Hopefulness Do you feel positive/motivated about your future?": "optim",
      "Resilience Are you able to bounce back from stressful events?": "resili",
      "How important is change to you?": "change",
      "# How close are you to where you want to be in managing your substance use?": "closemanag",
      "So, now we've gone through everything, how would you rate your situation over the last 4 weeks ?": "ratesituation",
      "Is there anything else you'd like to tell us about yourself ?":"else",
      "Are you engaged with any other services at the moment?": "otherserv",
      "DIRECTIONS SERVICES: What type of support best matches client needs and goals?":"services"

    },

    "values_table": {
        'I mostly feel safe in my home, but sometimes feel threatened' :'SafeAtHomeSometimesThreatened',
        'Yes - recently (in the last 4 weeks) (risk assessment required)': 'RiskAssesReqd',
        'Yes - in the past 4 weeks(risk assessment required)': 'RiskAssesReqd'
    },
    "bit_fields" : ['injshare', 'wrkdevorder'],
    "skip_fields" : [ ]

  }
  
}