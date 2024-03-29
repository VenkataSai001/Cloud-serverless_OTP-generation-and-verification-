import json
import boto3
import time
from random import randint

client_dynamo=boto3.resource('dynamodb')

table=client_dynamo.Table('otp_holder')

default_ttl = 120

def lambda_handler(event, context):
    
    email_id=event['queryStringParameters']['email_address']
    
    otp_value=randint(100000, 999999)
    
    entry={
    'email_id': email_id,
    'OTP': otp_value,
    'EXPIRATION_TIME': int(time.time()) + default_ttl
    }
    
    response=table.put_item(Item=entry)
    
    return "A verification code is sent to the email address you provided."