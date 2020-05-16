#!/usr/bin/env python3 

import boto3
import time

#s3 = boto3.resource('s3')
#for bucket in s3.buckets.all():
#    print(bucket.name)

client = boto3.client('athena')
query = "SELECT * FROM wine"
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
<<<<<<< HEAD
<<<<<<< HEAD
    # while loop
        # time module: wait a bit
    #return status\
    pass
=======
=======
>>>>>>> refs/remotes/origin/master
    print(execution_ID)
    for i in range(0,3):
        print("Query sent, waiting 10 seconds")
        time.sleep(10)
        try:
            response = client.get_named_query(NamedQueryId=execution_ID)
            if reponse:
                return response
                break
        except:
            pass
<<<<<<< HEAD
>>>>>>> 5d2768f... V1 wait for reponse

def get_results(status_message):
<<<<<<< HEAD
    pass

=======
    print("results")
>>>>>>> 6c3d4d0... Testing git from pycharm

def run_query():
    response = submit_query(query, database, s3_output)
<<<<<<< HEAD
    print("submitted query")
    status = wait_for_results(response)
    if status == "FAILED" | status == "CANCELLED":
=======
    print(f'{response}')
    status = wait_for_results(response['QueryExecutionId'])
    if status == "FAILED" or status == "CANCELLED":
>>>>>>> 5d2768f... V1 wait for reponse
=======

def get_results(status_message):
    print("results")

def run_query():
    response = submit_query(query, database, s3_output)
    print(f'{response}')
    status = wait_for_results(response['QueryExecutionId'])
    if status == "FAILED" or status == "CANCELLED":
>>>>>>> refs/remotes/origin/master
        print("query over")
        return 0
    elif status == "SUCCEEDED":
        print("Success?")
        get_results(status)
    else:
        print(status)
        print(response)


if __name__ == "__main__":
    run_query()
    print("tada!")
