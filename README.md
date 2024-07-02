# 라즈베리파이 물류로봇 프로젝트  

# 설치하는 법 
1. 가상환경 설정 
```
python3 -m venv venv 
```
2. pip로 필요한 라이브러리 설치
```
pip install -r requirements.txt
```
# 예제   
 

# 하드웨어 연결 

## 라즈베리파이 4 
- OS버전: 64bit bookworm

## 모터드라이버 
- [MDDS10](https://robu.in/wp-content/uploads/2015/08/MDDS10-Users-Manual.pdf) 

|GPIO#|기능|설명|
|------|---|--|
|12|AIN2|오른쪽 모터를위한  PWM 신호 입력|  
|13|AIN1|왼쪽 모터를 위한 PWM 신호 입력|
|19|DIG2|오른쪽 모터의 방향 신호 입력|
|16|DIG1|왼쪽 모터의 방향 신호 입력|

