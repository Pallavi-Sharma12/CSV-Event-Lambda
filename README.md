# CSV-Event-Lambda
Lambda function to read a csv file on S3 event and store data in sqlite3

1 - Lambda function picks the Key Name from the event of the specified bucket and store it in 'keyName'.

2 - Opens a sqlite DB connection.

3 - Gets the object from S3, using get_object with Bucket = <your bucket name> and Key = keyName (event based key detail)
 
4 - If the object ends with .csv, lambda reads the body of the object and store it in pandas dataframe.
 
5 - Using list comprehension, lambda read all the record from the dataframe and store it in toDB_Values and bulk insert the records in csvfile table of csvFile.db of sqlite3.
 
  
**Deploy - ** Create python virtual environment and perform pip install sqlite3 and pandas and upload the bundle to lambda function using AWS CLI command.
