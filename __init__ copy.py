
import os
import logging
import azure.functions as func
import pyodbc
import requests


server = 'tcp:hndserver.database.windows.net'
database = 'ansa_surveys'
username = 'mj'
envPwd = os.getenv('DBPWD')
password =  'Hit' 
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = None

def get_conn():
  if not cnxn:
    logging.warn('DB Connection was not initialized. Doing so now... ')
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
  return cnxn


def db_insert():
  params = (14, "Dinsdale")
  crsr = get_conn().cursor()
  crsr.execute("{CALL usp_UpdateFirstName (?,?)}", params)


def db_read():
    global cnxn
    results = []
    
    # if not cnxn:
    #     logging.warn('DB Connection was not initialized. Doing so now... ')
    #     cnxn = get_connection()
    
    cursor = get_conn().cursor()
    cursor.execute("SELECT * from ANSARaw_ITSPReview")
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]))
        results.append(str(row[0]) + " <> " + str(row[1]))        
        row = cursor.fetchone()
    return results


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    results = db_read()

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            aa =""
            if results and results[0]:
                aa = str(results[0])
            name = req_body.get('name') +aa

    if name:
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
