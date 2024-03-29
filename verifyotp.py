import json
import boto3
import time
client = boto3.client('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    
    email_id=event['queryStringParameters']['email_address']
    print("The received email id : {}".format(email_id))
    
    otp_from_user=event['queryStringParameters']['otp']
    print("The received otp : {}".format(otp_from_user))
    
    response = client.query(
    TableName='otp_holder',
    KeyConditionExpression='email_id = :email_id',
    ExpressionAttributeValues={
        ':email_id': {'S': email_id}
    },ScanIndexForward = False, Limit = 1)
    
    if(response['Count']==0):
        return "No such OTP was shared"
    else:
        latest_stored_otp_value=response['Items'][0]['OTP']['N']
        print("Latest Stored OTP Value : {}".format(latest_stored_otp_value))
        
        if(int(response['Items'][0]['EXPIRATION_TIME']['N'])<int(time.time())):
            return "Time Over"
        else:
            if(latest_stored_otp_value==otp_from_user):
                return "Verified"
            else:
                return "Wrong OTP"