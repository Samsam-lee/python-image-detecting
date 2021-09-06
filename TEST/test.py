import cv2

# 이미지 불러오기
# img = cv2.imread('0.png');
img = cv2.imread('0.png', cv2.IMREAD_GRAYSCALE);
# 이미지 사용자에게 보여주기
cv2.imshow("image", img);

# 동작 하기 전 키 누르는 것 대기
k = cv2.waitKey(0)

# 27 -> esc
if k == 27:
    cv2.destroyAllWindows();
# ord('s') -> s키
elif k == ord('s'):
    # 이미지 저장
    cv2.imwrite("grayTest.png",img)
    cv2.destroyAllWindows();