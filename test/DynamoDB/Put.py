from botocore.exceptions import ClientError

# Put
def put_user(Email, FirstName, LastName, Github, dynamodb):

    table = dynamodb.Table('user_table')
    
    try:
        response = table.put_item(
            Item={
                'Email': Email,
                'FirstName': FirstName,
                'LastName': LastName,
                'Github': Github
            })
    except ClientError as e:
        print(e.response['Error'['Message']])
    else:
        return['Item']
    
    return response