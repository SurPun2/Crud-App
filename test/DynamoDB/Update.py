from botocore.exceptions import ClientError

# Update
def update_user(Email, FirstName, LastName, Github, dynamodb=None):

    table = dynamodb.Table('user_table')

    try:
        response = table.update_item(
            Key={
                'Email': Email
            },
            UpdateExpression='SET FirstName = :val1, LastName = :val2, Github = :val3',
            ExpressionAttributeValues={
                ':val1': FirstName,
                ':val2': LastName,
                ':val3': Github
            })
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response