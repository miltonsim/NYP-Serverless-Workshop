# Import boto3 and uuid package 
import boto3, uuid

# Get the DynamoDB service resource
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id="YOUR-ACCESS-KEY",
    aws_secret_access_key="YOUR-SECRET-ACCESS-KEY",
    aws_session_token="YOUR-SESSION-TOKEN",
    region_name='us-east-1'
)

# Select the Product table
table = dynamodb.Table('Product')

# Generate a random unique product ID  
product_id = uuid.uuid4().hex

# Create product info 
product_info = { 
    "Id": product_id,
    "Name": "Huawei P30 Pro",
    "Cost": 30
}

# Put items into Product table
response = table.put_item(
   Item = product_info
)

# Print response where Status Code 200 denotes sucess 
print(response)