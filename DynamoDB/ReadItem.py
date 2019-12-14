# Import boto3 package 
import boto3

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

# Add in your product id that was generated 
product_id = "YOUR-PRODUCT-ID"

# Get item from Product table with product id 
response = table.get_item(
    Key = {
        "Id": product_id
    }
)

# Print response where Status Code 200 denotes sucess 
print(response)

# Retrieve product item from response
item = response['Item']

# Print out each column from product item
for column in item:
    print(column, item[column])

