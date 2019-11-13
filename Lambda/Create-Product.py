# Import json, boto3 and uuid packages 
import json, boto3, uuid

# Get the service resource
dynamodb = boto3.resource('dynamodb')
# Select the Product table
table = dynamodb.Table('Product')

def lambda_handler(event, context):
    # Generate a random unique product ID  
    product_id = uuid.uuid4().hex

    # Retrieve product name and cost from event 
    product_name = json.loads(event['body'])['Name']
    product_cost = json.loads(event['body'])['Cost']
    
    # Create product info 
    product_info = { 
        "Id": product_id,
        "Name": product_name
    }

    # Put items into Product table 
    response = table.put_item(
        Item = product_info
    )

    # Print response
    print(response)

    # Check if Status Code is 200    
    if response['ResponseMetadata']['HTTPStatusCode'] is 200:
        
        # Return Status Code
        return {
           'statusCode': 200
        }    