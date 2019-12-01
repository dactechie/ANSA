import pytest
from pprint import pprint
from SMSubmissionTrigger.db.operations import insert
from SMSubmissionTrigger.db import mydb



def test_insert_plain():
  mycol = mydb.get_collection('client_registration')
  result = insert(mycol,{"Cool":"haha",  "meta":{} })
  pprint(result)
