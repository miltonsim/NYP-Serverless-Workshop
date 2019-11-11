# Import json and boto3 packages 
import json, boto3

# Get the service resource
dynamodb = boto3.resource('dynamodb')
# Select the Product table
table = dynamodb.Table('Product')

def lambda_handler(event, context):
    # Scan table (retrieve all records)   
    response = table.scan()

    # Print response
    print(response)

    # Check if Status Code is 200    
    if response['ResponseMetadata']['HTTPStatusCode'] is 200:
        
        # Return Status Code and Items
        return {
           'statusCode': 200,
           'body': response['Items']
        }    