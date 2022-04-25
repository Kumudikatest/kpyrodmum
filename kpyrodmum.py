import boto3
cognito_idp = boto3.client("cognito-idp")
from os import environ

def handler(event, context):
    try:
        data = cognito_idp.list_users(
            UserPoolId=environ["UserPoolId_cognitokl"],
            Limit=10
        )
        print(data)
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
