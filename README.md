# AWS Lambda Functions

This repository contains two AWS Lambda functions:

1. **Lambda Function: Add Two Numbers**
   - This Lambda function takes two numbers as input and returns their sum.
   - **Deployment Instructions**:
     1. Create a new Lambda function in the AWS console.
     2. Upload the Python file `lambda_add_numbers.py`.
     3. Configure an appropriate IAM role to allow Lambda execution.
   - **Test**: You can trigger the Lambda function using a test event.

2. **Lambda Function: Store PDF in S3**
   - This Lambda function uploads a base64-encoded PDF file to an S3 bucket.
   - **Deployment Instructions**:
     1. Create a new Lambda function in the AWS console.
     2. Upload the Python file `lambda_upload_to_s3.py`.
     3. Set up an IAM role with permissions to upload to the specified S3 bucket (`s3:PutObject`).
   - **Test**: Trigger the Lambda function using a test event with base64 file data.

## How to Run the Project:
- To deploy and test the Lambda functions, follow the instructions above and use the AWS Lambda Console.
