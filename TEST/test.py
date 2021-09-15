# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import numpy

# gray 이미지 불러오기
# roadImage = cv2.imread('assets/TestTrack1.png', cv2.IMREAD_GRAYSCALE)
roadImage = cv2.imread('assets/testImage1.jpeg', cv2.IMREAD_GRAYSCALE)

# 가우시안 불러링은 일반적인 불러와 다르게 중심에 있는 픽셀에 높은 가중치 부여
# 세 번째 아규먼트를 0으로 하면 지정한 커널 크기에 맞추어 시그마를 계산해서 사용
blurImage = cv2.GaussianBlur(roadImage, (5, 5), 0)

# 테두리 따기
edgeImage = cv2.Canny(blurImage, 200, 200)

### 관심 영역 설정 (ROI) ###

# 이미지 크기
height, width = edgeImage.shape[:2]
print(height, width)

# 흑백 빈 이미지
mask = numpy.zeros_like(edgeImage)

ignore_mask_color = 255

vertices = numpy.array([[(-(width/4),height), ((width/2)-(width/10),(height/8)), 
                        ((width/2)+(width/10),(height/8)), (width+(width/4), height)]],dtype=numpy.int32)

# 관심 영역 지정 색으로 표현
cv2.fillPoly(mask, vertices, ignore_mask_color)

plt.figure(figsize=(10,8))
plt.imshow(mask,cmap='gray')
plt.show()

masked_image = cv2.bitwise_and(edgeImage, mask)

cv2.imshow('masked_image', masked_image)




# 이미지 사용자에게 보여주기
# cv2.imshow("Result Image", edgeImage)

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