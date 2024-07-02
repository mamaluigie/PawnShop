import os
import boto3
from typing import Dict
from tools import build_customer_profile_item

dynamodb = boto3.resource('dynamodb') 

# The event will look like this
#
# Sample Event:
# {
#     action: (one of 2, GET and PUT),
#     query: (some kind of combonation that can be queried in a dynamodb)
# }
#
#
# You will get the associated data with the GET request
# and you will get the response if it was successfull or not 
# for the PUT request
def handler(event: Dict[str, str], context: any):

    # Some error handling making sure that all of the required keys are there
    keys = ["action", "query"]
    response = None
    for key in event.keys():
        if (key not in keys):
            raise ValueError(f"Wrong key '{key}' in event")
        elif (len(event.keys()) != 2):
            raise ValueError(f"Only 2 arguments\n{len(event.keys())} gave")


    try: 
        table = dynamodb.Table(os.environ['DATABASE_NAME'])
        if event["action"].lower() == "put":
            print("entered the if statement")
            item = build_customer_profile_item("Mark", "Henry", "abc")
            print("built the item for the customer profile")
            try:
                print("Entered the try and about to try to send to the database")
                response = table.put_item(Item=item)
                print("PutItem succeeded:", response)
                return {
                    'statusCode': 200,
                    'body': 'Item successfully added to DynamoDB'
                }
            except Exception as e:
                print("Error putting item:", e)
                return {
                    'statusCode': 500,
                    'body': 'Failed to add item to DynamoDB'
                }
            
        elif event["action"].lower() == "get":
            pass
        else:
            raise ValueError(f"Wrong type of action gave. only give GET or PUT\n{event.action} gave")

    except:
        pass

    return response
