import boto3

#s3 = boto3.resource('s3')
#for bucket in s3.buckets.all():
#    print(bucket.name)


query = "SELECT * FROM wine"
database = "wine_feb_24"
s3_output = "s3://winebenathenaoutput/"

def submit_query(query, database, s3_output):
    client = boto3.client('athena')
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': database
        },
        ResultConfiguration={
            'OutputLocation': s3_output,
        }
    )
    print('Execution ID: ' + response['QueryExecutionId'])
    return response

def wait_for_results(execution_ID):
    # while loop
        # time module: wait a bit
    #return status\
    pass

def get_results(status_message):
    pass


def run_query():
    response = submit_query(query, database, s3_output)
    print("submitted query")
    status = wait_for_results(response)
    if status == "FAILED" | status == "CANCELLED":
        print("query over")
        return 0
    elif status == "SUCCEEDED":
        get_results(status)
    else:
        print(status)
        print(response)


if __name__ == "__main__":
    run_query()
    print("tada!")
