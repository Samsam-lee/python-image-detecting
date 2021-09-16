# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import numpy

# 이미지 불러오기
# image = cv2.imread('assets/TestTrack1.png')
# image = cv2.imread('assets/testImage1.jpeg')

# 영상 불러오기
video = cv2.VideoCapture('assets/testVideo1.mp4')

while(video.isOpened()):
    ret, image = video.read()
    try:
        # 이미지 크기
        height, width = image.shape[:2]
        print(height, width)
        
        # 이미지 흑백화
        roadImage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        # 가우시안 불러링은 일반적인 불러와 다르게 중심에 있는 픽셀에 높은 가중치 부여
        # 세 번째 아규먼트를 0으로 하면 지정한 커널 크기에 맞추어 시그마를 계산해서 사용
        blurImage = cv2.GaussianBlur(roadImage, (5, 5), 0)

        # 테두리 따기
        edgeImage = cv2.Canny(blurImage, 200, 200)

        ### 관심 영역 설정 (ROI) ###
        # 흑백 빈 이미지
        mask = numpy.zeros_like(edgeImage)

        ignore_mask_color = 255

        vertices = numpy.array([[(-(width/4),height), ((width/2)-(width/10),(height/8)), 
                                ((width/2)+(width/10),(height/8)), (width+(width/4), height)]],dtype=numpy.int32)

        # 관심 영역 지정 색으로 표현
        cv2.fillPoly(mask, vertices, ignore_mask_color)

        # plt.figure(figsize=(10,8))
        # plt.imshow(mask,cmap='gray')
        # plt.show()

        masked_image = cv2.bitwise_and(edgeImage, mask)

        # cv2.imshow('masked_image', masked_image)

        ### Hough Line ###
        rho = 2
        theta = numpy.pi/180
        threshold = 90
        min_line_len = 120
        max_line_gap = 150

        lines = cv2.HoughLinesP(masked_image, rho, theta, threshold, numpy.array([]), 
                                minLineLength = min_line_len, maxLineGap = max_line_gap)

        line_image = numpy.zeros((height, width, 3), dtype = numpy.uint8)

        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), [0, 0, 255], 5)

        # cv2.imshow('line_image', line_image)

    except:
        continue

    ### 원본 이미지에 차선 덮어쓰기 ###
    edgeLines = cv2.addWeighted(image, 0.8, line_image, 1, 0)

    cv2.imshow('edgeLines', edgeLines)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




# 동작 하기 전 키 누르는 것 대기
k = cv2.waitKey(0)

# 27 -> esc
if k == 27:
    cv2.destroyAllWindows();

# # ord('s') -> s키
# elif k == ord('s'):
#     # 이미지 저장
#     cv2.imwrite("test.png",img)
#     cv2.destroyAllWindows();