from .struct_transformers import flatten_team_staff, flatten_official_use
from .struct_transformers.initial_assessment import  (flatten_substance_use, flatten_everyday_living,
                                                     flatten_substance_impact, flatten_aod_history)

survey_mappings = {
    "struct_transform_funcs": (flatten_team_staff, flatten_official_use,  flatten_everyday_living,
                                 flatten_substance_use, flatten_substance_impact, flatten_aod_history),

    "incomplete_if_empty" : ("IMPACT OF SUBSTANCE USE.ni_goals", "HOUSING & SAFETY.ni_goals_housaft", 
                            "EVERYDAY LIVING.ni_goals_livissu", 
                            "PHYSICAL HEALTH & WELLBEING.ni_goals_welb", "MENTAL HEALTH & WELLBEING.ni_goals_ment",
                            "LEGAL.ni_goals_legal"),

    "numeric_fields" : ("injdays", "phyrate", "mentrate", "ndaysconsumed", "p1_5" ,"perday", "age1st", 
                        "closemanag" ,"qolrate", "Sex_ndays",  "Number of Days"),

    "field_table": {
      # "DEMOGRAPHICS"
      "Assessment Date" : "surv_date",
      "Your Directions/Pathways Details" : "team_staff",
      "SLK/Client ID": "client_id",

      # SUBSTSANCE USE
      # Note: Where is PDC ?????
      "How many days in the last 4 weeks?" : 'ndaysconsumed',
      "Principal Substance of Concern and Method of Use": "pdcmthd",
          "Please select from the dropdown menu": "selection",
      "Other substances of concern" :"odc",
          "Substance type - please select from the dropdown menu" : "type",
      "Injecting Drug Status": "inj",
          "How long since you last injected?": "injhwlong",
          "Shared Any Equipment?": "injshare",
          "Number of Injecting Days in the last 4 weeks?": "injdays",

      # "AOD History"
      "Do you ever think that your drug/alcohol use is out of control?": "outctrl",
      "Does the prospect of missing a session fix make you very anxious or nervous?" : "missanx",
      "How much do you worry about your use of drugs/alcohol?": "worry",
      "Do you wish you could stop?" : "stop",
      "How difficult would you find it to stop or go without your substance of concern?" : "diffstop",
        'Age of First Use': 'age1st',
        'Method of Use': 'method',
        'How Often?': 'freq',
        'How much per day?': 'perday',


      # IMPACT of SUBSTANCE USE
      "AOD Harms/Risks In the last 4 weeks, have you experienced any of the following risks?" : "exprisk",
      "Have you ever previously accessed alcohol and/or drug treatment?" : "prevassess",          #NOTE: not in ITSP
      "Did you gamble at all in the last 4 weeks ?": "gamble", #TODO make similar to rego :not Last but Past 4 weeks  ###
      "Did you engage in any other addictive behaviours in the last 4 weeks?": "addictiveb",
      "Impact on Daily Living During the last 4 weeks, how often has your substance use  impacted on your work or other daily living activities ?":"impactliving",
      "SUBSTANCE USE - CURRENT ISSUES Notes for ITSP":"ni_sum_pres_issues",
      "SUBSTANCE USE - GOALS Notes for ITSP": "ni_goals",
      "Usual Accommodation":  "usuaccom",
      "Living Arrangements - Who do you live with?": "livar",

      # "Housing and Safety
      "Housing Stability In the past 4 weeks, have you had any difficulties with housing or finding somewhere stable to live?": "diffhouse",
      "Physical Safety Do you feel safe where you live?" : "physafety",
      "Do you have any concerns for the safety and wellbeing of either yourself or others?": "safety_concern",
      "HOUSING & SAFETY - CURRENT ISSUES Notes for ITSP": "ni_hou_saft",
      "HOUSING & SAFETY - GOALS Notes for ITSP": "ni_goals_housaft",
        
      # EVERYDAY LIVING
      "What is your highest level of education?" : "highedu",                   #NOTE: not in ITSP
      "Are you currently employed?": "empl",
      "What is your principal income source?": "pinc",                           #NOTE: not in ITSP
      "In the last 4 weeks, how often have you engaged in any of the following?": "engag",
        "Frequency Daily/? times per week/Less than weekly/Not at all":"frequency",
          "Paid Work": "paidwork",
          "Voluntary Work": "volwork",
          "Study - college, school or vocational education": "eng_edu",
          "Looking after children": "lookafterchild",
          "Other caregiving activities": "othercaregiving",
        "How many days?": "ndays",
      "How much time per week do you spend on....?": "spendtime",
        "List your order of priority 1 - 5": "p1_5",
        "Time Spent" :"ts",
            "Drugs & Drinking": "drugdrink",
            "Hobbies, Sport & Recreation": "hobrec",
            "Family & Home": "famhom",
            "Me Time": "metime",
      "EVERYDAY LIVING - CURRENT ISSUES Notes for ITSP" : "ni_livissu",
      "EVERYDAY LIVING - GOALS Notes for ITSP": "ni_goals_livissu",
      
      
      # RISK # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      "Mental Health Risk Issues": "risk_ment_issues",
      "Any indication of mental health risks?": "risk_ment",
      "Any indication of domestic/family violence?": "risk_dv",
      "Any indication of suicidal ideation?": "risk_suicide",      
      "Have you experienced any thoughts of death/dying or of hurting yourself?": "thoughtsofhurt",
  
      # Physical Health
      "How has your physical health been, in the last 4 weeks?": "phyrate",
      "How often has your health caused problems in your daily life?": "phycauseprob", # change to physical healt caused problem ?
      "Do you have a GP or medical centre that you regularly attend?": "regumedic",   #NOTE: not in ITSP
      "In the past 4 weeks have you been in hospital or needed to call an ambulance?" : "ambu",      
      "Are you currently taking any medications?": "medications",
      "Do you suffer from any allergies?": "allerg",
      "PHYSICAL HEALTH & WELLBEING - CURRENT ISSUES Notes for ITSP": "ni_sum_welb",
      "PHYSICAL HEALTH & WELLBEING - GOALS Notes for ITSP":"ni_goals_welb",
      
      #Mental Health
      "How has your psychological/mental health been? Do you have moods, fears, emotions or other thoughts that concern you?":"mentrate",
      "Sleep Do you have any sleep issues? Check all that apply": "sleep",
      "How often does your mental health create problems in your daily life?": "mentcauseprob",
      "Have you ever been diagnosed with a mental health issue?" : "diagment",        #NOTE: not in ITSP
      "Have you have ever been hospitalised for a mental health issue?" : "hospment",
      "MENTAL HEALTH & WELLBEING - CURRENT ISSUES Notes for ITSP": "ni_sum_ment",
      "MENTAL HEALTH & WELLBEING - GOALS Notes for ITSP": "ni_goals_ment",
            
      # RELATIONSHIPS, PARENTING & SOCIAL WELLBEING
      "Social/Community Connections Do you have family and/or social connections who are positive and supportive? Are you involved in your community?":"socommconn",
      "How often does your substance use lead to problems or arguments with family members or friends?": "famprob",
      "Has anyone been violent or abusive towards you?": "violtoyou",
      "Have you used violence or been abusive towards anyone?": "violbyyou",
      "Parenting/Caregiving Do you have parenting/caregiving responsibilities? Are you the primary caregiver for, or living with, any children?" : "caregiving",
      "Are there any child protection concerns? Have either FaCS  or OCYFS  been involved with your family?": "childprot",
      "RELATIONSHIPS, PARENTING & SOCIAL WELLBEING - CURRENT ISSUES Notes for ITSP": "ni_rel",
      "RELATIONSHIPS, PARENTING & SOCIAL WELLBEING - GOALS Notes for ITSP": "ni_goals_rel",

      # LEGAL 
      "Have you served a custodial sentence in the past?": "custod",            #NOTE: not in ITSP
      "Legal Have you been arrested in the last 4 weeks?" : "arrest",
      "In the last 4 weeks, how often have you been involved in any illegal activities? ?": "illegal",
      "Are you currently subject to court orders or have any charges pending?": "crtorder",
      "Do you need help with a Work Development Order to pay off any outstanding fines?": "wrkdevorder",
      "LEGAL - CURRENT ISSUES Notes for ITSP": "ni_legal",
      "LEGAL - GOALS Notes for ITSP": "ni_goals_legal",
      
      # STRENGTHS
      "Optimism/Hopefulness Do you feel positive/motivated about your future?": "optim",
      "Resilience Are you able to bounce back from stressful events?": "resili",
      
      # Where are you at, right now ?
      "How important is change to you?": "change",
      "How close are you to where you want to be in managing your substance use?": "closemanag",
      "So, now we've gone through everything, how would you rate your situation over the last 4 weeks ?": "qolrate",
      "Is there anything else you'd like to tell us about yourself ?":"else",
      "Are you engaged with any other services at the moment?": "otherserv",

      # OFFICE USE ONLY
      "DIRECTIONS SERVICES: What type of support best matches client needs and goals?":"services",
    },

    "values_table": {
        'I mostly feel safe in my home, but sometimes feel threatened' :'SafeAtHomeSometimesThreatened',
        'Yes - recently (in the last 4 weeks) (risk assessment required)': 'RiskAssesReqd',
        'Yes - in the past 4 weeks(risk assessment required)': 'RiskAssesReqd',
        "Please select from the dropdown menu": "selection",

    },
    "bit_fields" : ['injshare', 'wrkdevorder'],
    "skip_fields" : [ ],

  }