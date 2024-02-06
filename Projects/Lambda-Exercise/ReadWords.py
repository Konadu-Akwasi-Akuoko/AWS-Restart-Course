import boto3
import re

s3 = boto3.client("s3")
sns = boto3.client("sns")


def lambda_handler(event, context):
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    file_obj = s3.get_object(Bucket=bucket_name, Key=key)

    file_content = file_obj["Body"].read().decode("utf-8")

    words = re.split(r"\s+", file_content)
    word_count = len(words)
    print(f"There are {word_count} words in {key}")

    sns.publish(
        TopicArn="arn:aws:sns:us-west-2:471112770419:AWSLambda",  # replace with your Topic ARN
        Message=f"The word count in the {key} file is {word_count}",
        Subject="Word Count Result",
    )

    return f"The word count in the {key} file is {word_count}"
