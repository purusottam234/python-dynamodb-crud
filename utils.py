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

# CRUD Operations for the business_user table
business_user_table_name = 'business_user'

# Create an item
def create_business_user_item(item):
    response = dynamodb.put_item(
        TableName=business_user_table_name,
        Item=item
    )
    print("Item created:", response)
    return response

# Read an item by email
def read_business_user_item(email):
    response = dynamodb.get_item(
        TableName=business_user_table_name,
        Key={'email': {'S': email}}
    )
    item = response.get('Item')
    return item

# Update an item by email
def update_business_user_item(email, update_expression, expression_values):
    response = dynamodb.update_item(
        TableName=business_user_table_name,
        Key={'email': {'S': email}},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_values
    )
    return response

# Delete an item by email
def delete_business_user_item(email):
    response = dynamodb.delete_item(
        TableName=business_user_table_name,
        Key={'email': {'S': email}}
    )
    return response


# CRUD Operations for the customer table
customer_table_name = 'customer'

# Create an item
def create_customer_item(item):
    response = dynamodb.put_item(
        TableName=customer_table_name,
        Item=item
    )
    return response

# Read an item by business_user_email and date_joined
def read_customer_item(business_user_email, date_joined):
    response = dynamodb.get_item(
        TableName=customer_table_name,
        Key={'business_user_email': {'S': business_user_email}, 'date_joined': {'S': date_joined}}
    )
    item = response.get('Item')
    return item

# Update an item by business_user_email and date_joined
def update_customer_item(business_user_email, date_joined, update_expression, expression_values):
    response = dynamodb.update_item(
        TableName=customer_table_name,
        Key={'business_user_email': {'S': business_user_email}, 'date_joined': {'S': date_joined}},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_values
    )
    return response

# Delete an item by business_user_email and date_joined
def delete_customer_item(business_user_email, date_joined):
    response = dynamodb.delete_item(
        TableName=customer_table_name,
        Key={'business_user_email': {'S': business_user_email}, 'date_joined': {'S': date_joined}}
    )
    return response