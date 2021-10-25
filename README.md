# python-image-detecting
Use OpenCV and practice YOLO, study python and use "AWS rekognition"

<br/>

ubuntu 18.04 <br/>
python에서 불러오기 <br/>
cuda (gpu) <br/>
jetson nano <br/>
darknet <br/>


## Windows 에서 Linux 설치
1. windows terminal 설치
2. wsl 설치
3. windows terminal 에서 linux 로 바로 열리게 설정
[https://wslhub.com/wsl-firststep/firststep/winterm/](https://wslhub.com/wsl-firststep/firststep/winterm/)
4. terminal을 열어도 windows가 아닌 linux 폴더로 열리게 변경

<br/>

## Darknet Install
- 출처 : pjreddie.com/darknet/install
```
git clone https://github.com/pjreddie/darknet.git
cd darknet
make
```
```
./darknet
```
했을 때
```
usage: ./darknet <function>
```
나오면 정상

<br/>

### Cuda
- https://elinux.org/Jetson/Installing_CUDA (쿠다 설치 공식 홈페이지)
- docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html
- developer.nvidia.com/cuda-11.1.0-download-archive?target_os=Linux&target_arch=x86_64&targetdistro=Ubuntu&target_version=1804&target_type=debnetwork

<br/>

## OpenCV
- jjeongil.tistory.com/1308
```
sudo apt install python3-opencv
```
<br/>

## 이미지 인식
```
./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
```

<br/>

## Jetson Nano
## 해상도 설정
~/.xsessionrc 파일 수정 (제일 아래 부분에 코드 추가)
```
echo "xrandr --fb 1280x720" >> ~/.xsessionrc
source ~/.xsessionrc
```

<br/>
