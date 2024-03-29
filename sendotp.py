import json
import boto3
client = boto3.client("ses")


def lambda_handler(event, context):
    print(event)
    if(event['Records'][0]['eventName']=='INSERT'):
        mail_id=event['Records'][0]['dynamodb']['Keys']['email_id']['S']
        print("The mail id is : {}".format(mail_id))
        
        otp=event['Records'][0]['dynamodb']['NewImage']['OTP']['N']
        print("The mail id is : {}".format(otp))
        
        body = """
                Use this code to verify your login at Simple Website<br>
                
                {}
             """.format(otp)
             
        message = {"Subject": {"Data": 'Your OTP (valid for only 2 mins)!'}, "Body": {"Html": {"Data": body}}}
        
        response = client.send_email(Source = '{FromAddress}', Destination = {"ToAddresses": [mail_id]}, Message = message) 
        
        print("The mail is sent successfully")