import sqlite3
import boto3
import pandas as pd
import io

def handler(event, context):
    try:
        keyName = event['Records'][0]['s3']['object']['key']
        con = sqlite3.connect('csvFile.db')
        cur = con.cursor()
        s3 = boto3.client('s3','ap-south-1')
        if keyName.endswith('.csv'):
            try:
                csvfile = s3.get_object(Bucket='lambda-csv-event', Key=keyName)
                contents = csvfile['Body'].read()
                df = pd.read_csv(io.BytesIO(contents), low_memory=False)
            except Exception as ex:
                print("[ERROR] " + str(ex))
                sns = boto3.client('sns','ap-south-1')
                response = sns.publish(TopicArn='<SNS Topic ARN>',Message="Hi\n\nMentioned exception has been occurred in handler lambda function. CSV file evaluation process aborts here.\n\n" + str(ex),)
                
            to_db = [(row['batch'], row['start'], row['end'], row['records'], row['pass'], row['message']) for index, row in df.iterrows()]
            print("to DB ")
            cur.executemany("INSERT INTO csvfile (batch, start, end, records, pass, message) VALUES (?, ?, ?, ?, ?, ?);", to_db)
            con.commit()
            con.close()
        else:
            print(f"{keyName} is not a CSV file")
    except Exception as ex:
        print("[ERROR] " + str(ex))
        sns = boto3.client('sns','ap-south-1')
        response = sns.publish(TopicArn='<SNS Topic ARN>',Message="Hi\n\nMentioned exception has been occurred in handler lambda function. CSV file evaluation process aborts here.\n\n" + str(ex),)
