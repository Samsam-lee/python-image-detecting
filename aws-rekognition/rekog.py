import csv
import boto3
import cv2

try:
    # aws rekognition 사용
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

    # 넘어온 response 값 안에서 객체의 위치 값이 넘어 오는 것만 구분
    for i in range(len(response['Labels'])):
        if response['Labels'][i]['Instances'] != []:
            print('Name : ', response['Labels'][i]['Name'])



except:
    print('error')







# if response['ResponseMetadata']['HTTPStatusCode'] != 200:
#     print('bug')


# for i in range(len(boxes)):
#     if i in indexes:
#         x, y, w, h = boxes[i]
#         label = str(classes[class_ids[i]])
#         color = colors[i]
#         # 사각형 그리는 함수
#         # img, start, end, color, thickness
#         cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
#         # image, text, text 시작 위치, font, font size, color, font bold
#         cv2.putText(img, label, (x, y+20), font, 2, color, 2)
#         # 정확성 출력
#         cfd = "confidence : %d%%"%int(confidences[i] * 100)
#         cv2.putText(img, cfd, (x, y+30), font, 1, color, 2)