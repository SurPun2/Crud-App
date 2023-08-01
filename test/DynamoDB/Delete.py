from botocore.exceptions import ClientError

# Delete
def delete_user(Email, dynamodb):

    table = dynamodb.Table('user_table')

    try:
        response = table.delete_item(Key={'Email': Email})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response