# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import numpy

# gray 이미지 불러오기
roadImage = cv2.imread('assets/TestTrack1.png', cv2.IMREAD_GRAYSCALE)
# roadImage = cv2.imread('assets/testImage1.jpeg', cv2.IMREAD_GRAYSCALE)

# 가우시안 불러링은 일반적인 불러와 다르게 중심에 있는 픽셀에 높은 가중치 부여
# 세 번째 아규먼트를 0으로 하면 지정한 커널 크기에 맞추어 시그마를 계산해서 사용
blurImage = cv2.GaussianBlur(roadImage, (5, 5), 0)

# 테두리 따기
edgeImage = cv2.Canny(blurImage, 50, 200)

# 관심 영역 설정 (ROI)

# height, width = edgeImage.shape[:2]
# print(height, width)

x=320; y=150; w=100; h=100        # roi 좌표
roi = edgeImage[y:y+h, x:x+w]         # roi 지정        ---①

print(roi.shape)                # roi shape, (50,50)
cv2.rectangle(roi, (0,0), (h-1, w-1), 255) # roi 전체에 사각형 그리기 ---②





# 이미지 사용자에게 보여주기
cv2.imshow("Result Image", edgeImage)





# # 다각형 모양 생성
# vertices = numpy.array([[(50,height),(width/2-45, height/2+60), (width/2+45, height/2+60), (width-50,height)]], dtype=numpy.int32)
# print(vertices)

# #
# mask = numpy.zeros_like(edgeImage)
# cv2.fillPoly(mask, vertices, 255)

# ROI_image = cv2.bitwise_and(edgeImage, mask)

# mark = numpy.copy(ROI_image)


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