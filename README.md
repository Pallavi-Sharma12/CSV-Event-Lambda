# CSV-Event-Lambda
Lambda function to read a csv file on S3 event and store data in sqlite3


Pre-requisite - 
  1 - Please make sure Lambda function has permission to S3, SNS service.
  2 - Timeout is more than 3 seconds
  3 - Runtime Settings, Handler = handler.handler
  4 - Create a virtual environment and install sqlite3, pandas and use cli command to upload the package on AWS Lambda
  5 - Create a test event on Lambda function with Event Template = Amazon S3 Put and in Records -> s3 -> bucket = provide your bucket name
