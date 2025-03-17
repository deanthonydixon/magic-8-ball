#!/bin/bash

# Zip the function code
zip -r lambda_function.zip .

# Deploy to AWS Lambda
aws lambda create-function --function-name Magic8BallFunction \
  --runtime python3.8 --role arn:aws:iam::381491856437:role/LambdaDynamoDBRole \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://lambda_function.zip
