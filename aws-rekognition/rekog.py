import csv
import boto3

with open('new_user_credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = 'roadImage.png'

client = boto3.client('rekognition',
                        aws_access_key_id = access_key_id,
                        aws_secret_access_key = secret_access_key)

with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

response = client.detect_labels(Image = {'Bytes': source_bytes},
                                MaxLabels=10)

print(response)