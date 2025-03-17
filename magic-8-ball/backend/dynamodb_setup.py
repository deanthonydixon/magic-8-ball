import boto3

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')

# Create the table
table_name = 'Magic8BallAnswers'

existing_tables = dynamodb.meta.client.list_tables()['TableNames']

if table_name not in existing_tables:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    )

    print(f"Creating table {table_name}...")
    table.wait_until_exists()
    print("Table created successfully!")
else:
    print(f"Table {table_name} already exists.")
