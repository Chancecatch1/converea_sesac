#### AIoT Converea(Automatic plant cultivation with AI) at SeSac

#### Title
- [AIoT Converea](https://energetic-bucket-84a.notion.site/AIoT-Converea-3c3d374c2acc4640a9c6ac2abf5c2cbe)

#### Schedule
- 2022-11 ~ 2022-12

#### Contents
- GPIO를 활용한 input, output 가능 여부 확인
- 온도, 습도, ph, 수위, 탁도 등의 sensor 정보 업데이트
- raspberry로 받은 sensor정보 Firestore DB에 업로드
- 식물의 성장도를 AI모델로 학습
- jetson nano에서 카메라 프레임을 열어, 식물의 성장도 계산
- jetson nano에 수집된 sensor정보 및 성장도를 Firestore DB에 업로드

#### Directory
- raspberry: 각종 sensor 및 firestore DB
- jetsonnano: socket통신, camera 및 firestore DB
- sensor: 온도, fanning, ph, water_level, pump etc..
