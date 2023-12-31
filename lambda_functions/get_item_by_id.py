import boto3
from botocore.exceptions import ClientError
from constants import TABLE_NAME
from helpers import buildResponse

# Initialize the DynamoDB client
dynamodb = boto3.client("dynamodb")


def lambda_handler(event, context):
    try:
        # Assuming the item id is passed as a query parameter
        item_id = str(event["queryStringParameters"]["id"]) or None
        if not item_id:
            return buildResponse(400, "ID is required")
        response = dynamodb.get_item(TableName=TABLE_NAME, Key={"id": {"S": item_id}})

        # Return not found if the item is not found
        if "Item" not in response:
            return buildResponse(400, "Item not found")

        # Return the item from the table
        return buildResponse(200, response["Item"])

    except ClientError as e:
        print(e.response["Error"]["Message"])
        return buildResponse(500, e.response["Error"]["Message"])
    except Exception as e:
        print(e)
        return buildResponse(500, str(e))
