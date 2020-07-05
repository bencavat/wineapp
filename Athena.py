#!/usr/bin/env python3 

import boto3
import time
import sys
import json
from wineapp.jsonparsing import dump_clean_data

client = boto3.client('athena')
query = "SELECT * FROM wine WHERE acidity >= 2"
database = "wine_feb_24"
s3_output = "s3://winebenathenaoutput/"
savefile = "raw data"
json_file = "dump.json"


def submit_query(query, database, s3_output):
    response = client.start_query_execution(
        QueryString=query, QueryExecutionContext={'Database': database},
        ResultConfiguration={'OutputLocation': s3_output}
    )
    print('Execution ID: ' + response['QueryExecutionId'])
    return response


def save_results(results, savefile):
    with open(savefile, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)


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
        # now you gotta parse the json
        # give random wines
        print(results)
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
    #[save_results(results, savefile) if results else print("No results, no savefile")]
    dump_clean_data(results["ResultSet"]["Rows"], json_file)


if __name__ == "__main__":
    main()
