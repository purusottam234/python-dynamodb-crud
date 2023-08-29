import os
import boto3
from botocore.exceptions import ClientError

# Replace these with your own credentials and region
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
region_name = 'ap-south-1'

dynamodb = boto3.client(
    'dynamodb', 
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

table_name = 'business_user'

"""
Do not include all the Key values in the attribute-definitions and key-schema. 
Only include the HASH and RANGE keys in these while creating table.
When you are inserting an item into dynamo, it will accept other keys too that were no defined in the above attributes/schema.
"""

attribute_definitions = [
    {
        'AttributeName': 'email',
        'AttributeType': 'S'
    },
    # {
    #     'AttributeName': 'is_superuser',
    #     'AttributeType': 'B'
    # },
    # {
    #     'AttributeName': 'first_name',
    #     'AttributeType': 'S'
    # },
    # {
    #     'AttributeName': 'last_name',
    #     'AttributeType': 'S'
    # },
    # {
    #     'AttributeName': 'is_active',
    #     'AttributeType': 'B'
    # },
    # {
    #     'AttributeName': 'date_joined',
    #     'AttributeType': 'S'
    # },
    # {
    #     'AttributeName': 'company_name',
    #     'AttributeType': 'S'
    # },
    # {
    #     'AttributeName': 'broker_service',
    #     'AttributeType': 'S'
    # },
    # {
    #     'AttributeName': 'broker_api_key',
    #     'AttributeType': 'S'
    # }
]

key_schema = [
    {
        'AttributeName': 'email',
        'KeyType': 'HASH'
    }
]

# Define the provisioned throughput settings
provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}

# Attempt to create the table, handling the case where it already exists
try:
    response = dynamodb.create_table(
        TableName=table_name,
        AttributeDefinitions=attribute_definitions,
        KeySchema=key_schema,
        ProvisionedThroughput=provisioned_throughput
    )
    print("Table created successfully!")
except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceInUseException':
        print("Table already exists.")
    else:
        print("An error occurred:", e)


# Define the table schema for the "customer" table
customer_table_name = 'customer'
customer_attribute_definitions = [
    {
        'AttributeName': 'business_user_email',
        'AttributeType': 'S'
    },
    {
        'AttributeName': 'date_joined',
        'AttributeType': 'S'
    },
    # {
    #     'AttributeName': 'customer_name',
    #     'AttributeType': 'S'
    # },
    # {
    #     'AttributeName': 'customer_broker_id',
    #     'AttributeType': 'S'
    # },
    # {
    #     'AttributeName': 'investment_style',
    #     'AttributeType': 'S'
    # },
    # {
    #     'AttributeName': 'investment_strategy',
    #     'AttributeType': 'S'
    # },
    # {
    #     'AttributeName': 'trading_ability',
    #     'AttributeType': 'B'
    # }
]

customer_key_schema = [
    {
        'AttributeName': 'business_user_email',
        'KeyType': 'HASH'
    },
    {
        'AttributeName': 'date_joined',
        'KeyType': 'RANGE'
    }
]

# Define the provisioned throughput settings for the "customer" table
customer_provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}

# Attempt to create the "customer" table, handling the case where it already exists
try:
    customer_response = dynamodb.create_table(
        TableName=customer_table_name,
        AttributeDefinitions=customer_attribute_definitions,
        KeySchema=customer_key_schema,
        ProvisionedThroughput=customer_provisioned_throughput
    )
    print("Customer table created successfully!")
except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceInUseException':
        print("Customer table already exists.")
    else:
        print("An error occurred:", e)