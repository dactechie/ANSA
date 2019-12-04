
"""App configuration."""
from os import environ

SM_BEARER_TOKEN = environ.get('SM_BEARER_TOKEN')

REGO_LOGICAPP_URI = environ.get('REGO_LOGICAPP_URI')
INITIAL_ASSESSMENT_LOGICAPP_URI = environ.get('INITIAL_ASSESSMENT_LOGICAPP_URI')
ITSP_LOGICAPP_URI = environ.get('ITSP_LOGICAPP_URI')

ANSA_MONGO = environ.get('ANSA_MONGO')
