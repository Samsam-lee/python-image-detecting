import cv2
import numpy

# Yolo 로드
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# classes -> 학습된 객체 이름
classes = []

with open("coco.names", "rt") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = numpy.random.uniform(0, 255, size=(len(classes), 3))

video = cv2.VideoCapture('assets/driveRoad.mov')

while(video.isOpened()):
    ret, img = video.read()

    try:
        # 이미지 가져오기
        # img = cv2.imread("assets/personInRoad.jpg")
        # img = cv2.resize(img, None, fx=0.4, fy=0.4)
        # img = cv2.resize(img, dsize=(416,416))
        height, width, channels = img.shape

        # Detecting objects
        # cv2.dnn.blobFromImage -> image, scalefactor, size, mean, swapRB, crop, ddepth
        # scalefactor : 입력 영상 픽셀 값에 곱할 값, 기본 값은 1
        # size : 출력 영상의 크기, 기본 값은 (0, 0)
        # mean : 입력 영상 각 채널에서 뺄 평균 값, 기본 값은 (0, 0, 0, 0)
        # swapRB : R과 B채널을 서로 바꿀 것인지를 결정하는 플래그, 기본 값은 False
        # crop : crop 수행 여부, 기본 값은 False
        # ddepth : 출력 블롭의 깊이, CV_32F or CV_8U, 기본 값은 CV_32F
        # 반환 값 : shape = (N, C, H, W), N은 갯수, C는 채널 갯수, HW는 영상 크기
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        # 네트워크 입력 설정
        net.setInput(blob)
        # outs -> 감지 결과
        outs = net.forward(output_layers)

        # print(outs)

        # 정보를 화면에 표시
        class_ids = []
        confidences = []
        boxes = []

        # Object detected
        for out in outs:
            # detection 배열의 index 5번부터 끝까지를 활용하여 confidence 확인
            for detection in out:
                scores = detection[5:]
                class_id = numpy.argmax(scores)
                confidence = scores[class_id]
                
                # 신뢰성 50% 이상일 때
                if confidence > 0.5:
                    # for i in detection[:5]:
                    #     print(i)
                    # print('-------------------')
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    # 좌표
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)


        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        # print(confidences)

        # font = cv2.FONT_HERSHEY_SIMPLEX
        font = cv2.FONT_HERSHEY_PLAIN
        # font = cv2.FONT_HERSHEY_DUPLEX
        # font = cv2.FONT_HERSHEY_COMPLEX
        # font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        # font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        # font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        # font = cv2.FONT_ITALIC

        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[i]
                # 사각형 그리는 함수
                # img, start, end, color, thickness
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                # image, text, text 시작 위치, font, font size, color, font bold
                cv2.putText(img, label, (x, y+20), font, 2, color, 2)
                # 정확성 출력
                cfd = "confidence : %d%%"%int(confidences[i] * 100)
                cv2.putText(img, cfd, (x, y+30), font, 1, color, 2)
    except:
        continue

    if type(img) == type(None):
        break

    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cv2.waitKey(0)
cv2.destroyAllWindows()

# 영상의 프레임이 끊기는 이유
## GPU 로 실행을 해야 조금 더 빠르다고 한다.
## 텐서 플로우 임포트 하는 것 알아보기
## 다른 사람들 예제 많이 찾아보기