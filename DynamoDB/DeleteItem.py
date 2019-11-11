# Import boto3 package 
import boto3

# Get the DynamoDB service resource
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id="YOUR-ACCESS-KEY",
    aws_secret_access_key="YOUR-SECRET-ACCESS-KEY",
    region_name='us-east-1'
)

# Select the Product table
table = dynamodb.Table('Product')

# Add in your product id that was generated 
product_id = "YOUR-PRODUCT-ID"

# Delete item from Product table with product id  
response = table.delete_item(
    Key = {
        "Id": product_id
    }
)

# Print response where Status Code 200 denotes sucess 
print(response)