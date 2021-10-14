import csv
import boto3
from PIL import Image, ImageDraw

try:
    # aws rekognition 사용
    with open('new_user_credentials.csv', 'r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[2]
            secret_access_key = line[3]

    photo = 'roadImage.png'
    img = Image.open(photo)
    imgWidth, imgHeight = img.size
    draw = ImageDraw.Draw(img)

    client = boto3.client('rekognition',
                            aws_access_key_id = access_key_id,
                            aws_secret_access_key = secret_access_key)

    with open(photo, 'rb') as source_image:
        source_bytes = source_image.read()

    response = client.detect_labels(Image = {'Bytes': source_bytes},
                                    MaxLabels=10,
                                    MinConfidence=75)
    print(response)

    # 넘어온 response 값 안에서 객체의 위치 값이 넘어 오는 것만 구분
    labels = response['Labels']

    for i in range(len(labels)):
        if labels[i]['Instances'] != []:
            print('Name : ', labels[i]['Name'])

            for j in range(len(labels[i]['Instances'])):
                box = labels[i]['Instances'][j]['BoundingBox']

                left = imgWidth * box['Left']
                top = imgHeight * box['Top']
                width = imgWidth * box['Width']
                height = imgHeight * box['Height']

                points = (
                    (left,top),
                    (left + width, top),
                    (left + width, top + height),
                    (left , top + height),
                    (left, top)
                )
                draw.line(points, fill='#00d400', width=2)

except:
    print('error')

img.show()