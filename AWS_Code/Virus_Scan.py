import http
import urllib.parse as urlparse
import json

def lambda_handler(event, context):
    for record in event["Records"]:
        key    = record["s3"]["object"]["key"]
        bucket = record["s3"]["bucket"]["name"]
        url    = "https://moj-s3-virus-scan.dsd.io/scan?" + urlparse.urlencode({"key": key, "bucket": bucket})
        print("url: " + url)
        http.client.HTTPConnection.request("GET", url)
    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }