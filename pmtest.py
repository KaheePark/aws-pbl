# import pymysql
# import boto3
#
# ssm = boto3.client('ssm')
# parameter = ssm.get_parameter(Name='/myweb/database1_password',WithDecryption = True)
# db_password= parameter['Parameter']['Value']
#
# conn = pymysql.connect(host='database-1.cltmc8lqcf9q.ap-northeast-2.rds.amazonaws.com', port=3306, db='pbldb', passwd=db_password, user='admin')
# print(conn)

#

import boto3
ssm = boto3.client('ssm')
parameter = ssm.get_parameter(Name='/myweb/database1_password', WithDecryption = True)
db_password= parameter['Parameter']['Value']
print(db_password)

import boto3
def upload_file_to_bucket(file_name):
    BUCKET_NAME = 's3-gaheeboard-files'
    S3_KEY = 'images/' + file_name
    s3 = boto3.client('s3')
    s3.upload_file(file_name, BUCKET_NAME, S3_KEY)

file_name='banana.jfif'
upload_file_to_bucket(file_name)
