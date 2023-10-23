import boto3
from botocore.exceptions import ClientError
from helpers import buildResponse

# Initialize the DynamoDB client
dynamodb = boto3.client("dynamodb")


def lambda_handler(event, context):
    try:
        response = dynamodb.scan(TableName="JittoItems")

        # Return the items from the table
        return buildResponse(200, response.get("Items", []))

    except ClientError as e:
        print(e.response["Error"]["Message"])
        return buildResponse(500, e.response["Error"]["Message"])
    except Exception as e:
        print(e)
        return buildResponse(500, str(e))
