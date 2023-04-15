import boto3

def send_email(to, subject, body):
    ses = boto3.client('ses', region_name='us-east-1')
    response = ses.send_email(
        Source='klucse2000030533@gmail.com',
        Destination={
            'ToAddresses': [to]
        },
        Message={
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Text': {
                    'Data': body
                }
            }
        }
    )
    return response

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    table_name = 'emails'
    response = dynamodb.scan(TableName=table_name)
    for item in response['Items']:
        email = item['email']['S']
        subject = 'sample email'
        body = 'This is a test email sent from Lambda'
        response = send_email(email, subject, body)
        print(response)
