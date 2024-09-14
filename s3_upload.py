import boto3

s3 = boto3.client('s3', aws_access_key_id='', \
                  aws_secret_access_key= '')
s3.upload_file('C:\\Users\\abrvarun\\Documents\\tools\\s3_upload\\Health_Sleep_Statistics.csv', \
               'test-14092024', 'test_upload/Health_Sleep_Statistics.csv')