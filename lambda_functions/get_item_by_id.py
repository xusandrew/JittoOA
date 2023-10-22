import boto3
import json
from botocore.exceptions import ClientError

# Initialize the DynamoDB client
dynamodb = boto3.client("dynamodb")


def lambda_handler(event, context):
    try:
        item_id = str(event["id"]) or None
        if not item_id:
            return {"statusCode": 400, "body": "ID is required"}
        response = dynamodb.get_item(TableName="JittoItems", Key={"id": {"S": item_id}})

        if "Item" not in response:
            return {"statusCode": 400, "body": "Item not found"}

        # Extract the 'Item' from the response and stringify it
        item_data = json.dumps(response["Item"])

        return {"statusCode": 200, "body": item_data}
    except ClientError as e:
        print(e.response["Error"]["Message"])
        return {"statusCode": 500, "body": e.response["Error"]["Message"]}
    except Exception as e:
        print(e)
        return {"statusCode": 500, "body": str(e)}
