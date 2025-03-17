import json
import random
import boto3
from datetime import datetime

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Magic8BallAnswers')

# Default answers
DEFAULT_ANSWERS = [
    "Yes", "No", "Maybe", "Ask again later",
    "Definitely", "I wouldn't count on it", "Absolutely!", "Unclear, try again"
]

def lambda_handler(event, context):
    if event.get("httpMethod") == "GET":
        return get_random_answer()
    elif event.get("httpMethod") == "POST":
        return add_custom_answer(event)
    else:
        return {"statusCode": 400, "body": json.dumps("Unsupported method")}

def get_random_answer():
    # Fetch custom answers from DynamoDB
    response = table.scan()
    custom_answers = [item["answer"] for item in response.get("Items", [])]

    all_answers = DEFAULT_ANSWERS + custom_answers
    random_answer = random.choice(all_answers)

    return {
        "statusCode": 200,
        "body": json.dumps({"answer": random_answer})
    }

def add_custom_answer(event):
    body = json.loads(event.get("body", "{}"))
    new_answer = body.get("answer")

    if not new_answer:
        return {"statusCode": 400, "body": json.dumps("No answer provided")}

    table.put_item(Item={"id": str(datetime.utcnow()), "answer": new_answer})

    return {"statusCode": 201, "body": json.dumps("Answer added successfully")}
