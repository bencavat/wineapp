#!/usr/bin/env python3 

import boto3
import time
import sys
import json
from wineapp.jsonparsing import dump_clean_data

'''
Athena.py pings Athena on AWS with a specific SQL search
- The output can be sent to the file "raw data"
- Output can also be assigned to a json var
'''

client = boto3.client('athena')
query = "SELECT * FROM wine WHERE acidity >= 2"
database = "wine_feb_24"
s3_output = "s3://winebenathenaoutput/"
savefile = "raw data"
json_file = "dump.json"

# Run a SQL query on an S3 database and send results to an S3_output bucket. Return
def submit_query(query, database, s3_output):
    response = client.start_query_execution(
        QueryString=query, QueryExecutionContext={'Database': database},
        ResultConfiguration={'OutputLocation': s3_output}
    )
    print('Execution ID: ' + response['QueryExecutionId'])
    return response

def wait_for_results(execution_ID):
    for i in range(0,5):
        try:
            response = client.get_query_execution(QueryExecutionId=execution_ID)
            status = response['QueryExecution']['Status']['State']
            print(status)
            if status == "SUCCEEDED" or status == "FAILED" or status == "CANCELLED":
                return status
            else:
                time.sleep(10)
        except:
            return 0


def get_query_results(response):
    status = wait_for_results(response['QueryExecutionId'])
    if status == "SUCCEEDED":
        results = client.get_query_results(QueryExecutionId=response['QueryExecutionId'])
        print("Success!")
        return results
    elif status == "FAILED" or status == "CANCELLED":
        print(f"query over: status is {status}")
        sys.exit()
    else:
        results = client.get_query_results(QueryExecutionId=response['QueryExecutionId'])
        print("couldn't assess status")
        print(f'Status is:\n {status}')
        print(f'Response is:\n {response}')
        print(f'results is:\n {results}')


def main():
    response = submit_query(query, database, s3_output)
    results = get_query_results(response)
    dump_clean_data(results["ResultSet"]["Rows"], json_file)


if __name__ == "__main__":
    main()
