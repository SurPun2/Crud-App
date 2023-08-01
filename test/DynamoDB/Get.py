from botocore.exceptions import ClientError

# Get
def get_user(Email, dynamodb):

    table = dynamodb.Table('user_table')

    try:
        response = table.get_item(Key={'Email': Email})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']
