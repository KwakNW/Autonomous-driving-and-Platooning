# POSCO 청년 AI BigData 아카데미 AI 프로젝트

<h5>사용 언어 및 Tool</h5>

- Python
- Raspberry Pi
- Ubuntu
- Cuda 10.2

<h5> 서버 시스템 구성도 </h5>

![Untitled Diagram](https://user-images.githubusercontent.com/68180545/139644414-0de2d4e6-75f8-4ed2-ae03-e26e6b844511.png)

<h5> 하드웨어 </h5>

![image](https://user-images.githubusercontent.com/68180545/139644511-c917a194-bb69-438b-9155-d4658f4efad3.png)
![image](https://user-images.githubusercontent.com/68180545/139644549-9b20ac25-a367-4433-aa8a-593ec3a44a5e.png)

<h5> 소프트웨어 </h5>

1. TCP/IP & Bluetooth Socket 기반 서버
- 라즈베리파이 연산 능력을 초과하는 연산을 workstation에서 처리
- 간단한 주행 신호는 Bluetooth 통신으로 처리 (신호 체계와 같은)

2. V2X 기반 제어 코딩
- V2N : 교통상황을 제공받아 네트워크가 차량을 판단 및 주행제어
- V2V : 차량 간 통신 제어, 군집주행
- V2I : 차량과 인프라 간 통신, 신호체계 제어
- V2X : 차량이 네트워크를 통해 다른 차량 및 인프라가 구축된 사물과 정보를 교환하는 통신 기술
![image](https://user-images.githubusercontent.com/68180545/139645462-0fb4b1a7-efba-4cac-8fd0-ccae299a172b.png)

3. Lane Detection
- 사진에서 선을 인식하고 두 선의 각도 차이를 통해 직진, 좌회전, 우회전 명령을 내림
- gray scale을 적용하여 속도를 높힘

![image](https://user-images.githubusercontent.com/68180545/139645141-665c19a6-a036-4ad1-88ed-53a2f4b5f381.png)

4. YOLO

표지판 및 차량을 학습시켜 사용하려했으나 GPU 위에 올라가지 않고 CPU상에서 운영되는 문제로 사용X

![image](https://user-images.githubusercontent.com/68180545/139645710-656b5b56-1d58-4944-a097-68e38dee9c50.png)

5. Depth
MobileNet 모델을 사용하여 앞 차를 인지하고 Depth 카메라를 통해 거리 측정 및 속도 조절 수행
![image](https://user-images.githubusercontent.com/68180545/139645982-078c5b8f-16be-4eb9-b01a-a49e5c9db12e.png)
