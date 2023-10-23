import boto3
import json
from uuid import uuid4
from helpers import buildResponse
from botocore.exceptions import ClientError

# Initialize the DynamoDB client
dynamodb = boto3.client("dynamodb")


def lambda_handler(event, context):
    try:
        # Assuming the item data is passed in the event body
        if isinstance(event["body"], str):
            item_data = json.loads(event["body"])
        else:
            item_data = event["body"]

        # Extract required fields or validate as needed. Example:
        if "name" not in item_data or "description" not in item_data:
            return buildResponse(400, "'name', and 'description' are required")

        # Generate a unique id for the item
        itemId = item_data.get("id") or str(uuid4())
        item_data["id"] = itemId

        resultItem = {}
        for key, value in item_data.items():
            resultItem[key] = {"S": value}

        # Insert the item into the table
        dynamodb.put_item(TableName="JittoItems", Item=resultItem)

        # Return success response
        return buildResponse(200, "Item added successfully with id " + itemId)

    except ClientError as e:
        print(e.response["Error"]["Message"])
        return buildResponse(500, e.response["Error"]["Message"])
    except Exception as e:
        print(e)
        return buildResponse(500, str(e))
