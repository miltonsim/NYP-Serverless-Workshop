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

# Update item's cost to 50 from Product table with product id  
response = table.update_item(
    Key = {
        "Id": product_id
    },
    UpdateExpression='SET Cost = :val1',
    ExpressionAttributeValues={
        ':val1': 50
    }
)

# Print response where Status Code 200 denotes sucess 
print(response)