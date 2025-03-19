#1serverless
!pip install awscli
!aws configure
#2
%%writefile lambda_function.py
import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from AWS Lambda!')
    }
#3
!zip function.zip lambda_function.py
#4
%%writefile trust-policy.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "lambda.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
#5
!aws iam create-role --role-name lambda-execution-role \
    --assume-role-policy-document file://trust-policy.json
#6
!aws lambda create-function --function-name MyServerlessFunction \
    --runtime python3.8 \
    --role arn:aws:iam::061039770856:role/lambda-execution-role \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://function.zip
!aws apigatewayv2 create-api --name "MyServerlessAPI" \
    --protocol-type HTTP
!aws lambda add-permission --function-name MyServerlessFunction \
    --statement-id apigateway-test \
    --action lambda:InvokeFunction \
    --principal apigateway.amazonaws.com
!aws apigatewayv2 create-stage --api-id 4jsbafrzw0 \
    --stage-name prod --auto-deploy
!aws apigatewayv2 get-integrations --api-id 4jsbafrzw0
!aws apigatewayv2 create-route --api-id 4jsbafrzw0 \
    --route-key "ANY /" \
    --target "integrations/an91oip"
!aws apigatewayv2 get-routes --api-id 4jsbafrzw0
!curl https://4jsbafrzw0.execute-api.us-east-1.amazonaws.com/prod/