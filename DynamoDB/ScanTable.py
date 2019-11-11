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

# Scan table (retrieve all records)   
response = table.scan()

# Print response where Status Code 200 denotes sucess 
print(response)

# Retrieve product items from response
items = response['Items']

# Print out each column from product item from all product items
for item in items: 
    for column in item:
        print(column, item[column])   