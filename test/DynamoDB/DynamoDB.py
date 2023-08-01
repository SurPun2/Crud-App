# Create DynamoDB table 'user_table' with the primary-key (Email)
def create_user_table(dynamodb):

    table = dynamodb.create_table(
        TableName='user_table',
        KeySchema=[
            {
                'AttributeName': 'Email',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'Email',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    
    return table