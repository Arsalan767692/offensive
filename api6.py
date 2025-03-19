#1
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


#2
!echo 'def lambda_handler(event, context): return {"statusCode": 200, "body": "Hello from API Gateway!"}' > lambda_function.py
!zip function.zip lambda_function.py
!aws iam create-role --role-name lambda-execution-role \
    --assume-role-policy-document file://trust-policy.json
!aws lambda create-function --function-name MyFunction \
    --runtime python3.9 \
    --role arn:aws:iam::061039770856:role/lambda-execution-role \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://function.zip
!aws apigatewayv2 create-api --name MyHttpApi \
    --protocol-type HTTP
!aws lambda get-function --function-name MyFunction
!aws apigatewayv2 create-integration --api-id xnxwod7226 --integration-type AWS_PROXY --integration-uri arn:aws:lambda:us-east-1:061039770856:function:MyFunction --payload-format-version "2.0"
!aws apigatewayv2 get-integrations --api-id xnxwod7226
!aws apigatewayv2 create-route --api-id xnxwod7226 \
    --route-key "POST /process" \
    --target "integrations/pie7tjp"
!aws apigatewayv2 create-stage --api-id xnxwod7226 \
    --stage-name prod --auto-deploy
!aws lambda add-permission --function-name MyFunction \
    --statement-id apigateway-invoke \
    --action lambda:InvokeFunction \
    --principal apigateway.amazonaws.com \
    --source-arn arn:aws:execute-api:us-east-1:061039770856:xnxwod7226/*

!aws apigatewayv2 get-apis
!curl -X POST -H "Content-Type: application/json" -d '{"input": "hello world"}' https://xnxwod7226.execute-api.us-east-1.amazonaws.com/prod/process

