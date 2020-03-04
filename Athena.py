import boto3

#s3 = boto3.resource('s3')
#for bucket in s3.buckets.all():
#    print(bucket.name)


query = "SELECT * FROM wine"
database = "wine_feb_24"
s3_output = "s3://winebenathenaoutput/"

def run_query(query, database, s3_output):
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
