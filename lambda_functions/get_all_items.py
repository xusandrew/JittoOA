import boto3
from botocore.exceptions import ClientError

# Initialize the DynamoDB client
dynamodb = boto3.client("dynamodb")


def lambda_handler(event, context):
    try:
        response = dynamodb.scan(TableName="JittoItems")

        # Return the items from the table
        return {"statusCode": 200, "body": response.get("Items", [])}

    except ClientError as e:
        print(e.response["Error"]["Message"])
        return {"statusCode": 500, "body": e.response["Error"]["Message"]}
    except Exception as e:
        print(e)
        return {"statusCode": 500, "body": str(e)}
