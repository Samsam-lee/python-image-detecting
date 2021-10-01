import cv2
import numpy

# Yolo 로드
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = numpy.random.uniform(0, 255, size=(len(classes), 3))

# 이미지 가져오기
img = cv2.imread("personInRoad.jpg")
img = cv2.resize(img, None, fx=0.4, fy=0.4)
height, width, channels = img.shape

# Detecting objects
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
# outs -> 감지 결과
outs = net.forward(output_layers)

print(outs)

# 정보를 화면에 표시
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = numpy.argmax(scores)
        confidence = scores[class_id]
        
        # 신뢰성 50% 이상일 때
        if confidence > 0.5:
            # Object detected
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
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
        # image, text, text 시작 위치, font, font size, color, font bold
        cv2.putText(img, label, (x, y), font, 1, color, 1)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

