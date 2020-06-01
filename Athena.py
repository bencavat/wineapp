#!/usr/bin/env python3 

import boto3
import time

client = boto3.client('athena')
query = "SELECT * FROM wine WHERE acidity >= 2"
database = "wine_feb_24"
s3_output = "s3://winebenathenaoutput/"


def submit_query(query, database, s3_output):
    response = client.start_query_execution(
        QueryString=query, QueryExecutionContext={'Database': database},
        ResultConfiguration={'OutputLocation': s3_output}
    )
    print('Execution ID: ' + response['QueryExecutionId'])
    return response


def wait_for_results(execution_ID):
    # while loop
        # time module: wait a bit
    #return status\
    for i in range(0,3):
        print("Query sent, waiting 10 seconds")
        time.sleep(10)
        try:
            status = client.get_query_execution(QueryExecutionId=execution_ID)
            if status:
                results = client.get_query_results(QueryExecutionId=execution_ID)
                return status, results
            else:
                print("Trying again")
        except:
            return 0

def run_query(response):
    status, results = wait_for_results(response['QueryExecutionId'])
    if status == "FAILED" or status == "CANCELLED":
        print("query over")
        return 0
    elif status == "SUCCEEDED":
        print("Success?")
        print(results)
    else:
        print("couldn't assess status")
        print(f'Status is:\n {status}')
        print(f'Response is:\n {response}')
        print(f'results is:\n {results}')

def main():
    response = submit_query(query, database, s3_output)
    run_query(response)


if __name__ == "__main__":
    main()
