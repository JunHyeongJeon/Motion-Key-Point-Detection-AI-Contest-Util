# 모션 키포인트 검출 AI 경진대회 관련 유틸리티 코드

### Intro
Dacon에서 개최하는 [모션 키포인트 검출 AI 경진대회](https://dacon.io/competitions/official/235701/overview/description/)에서 AI 모델을 개발하면서 필요한 유틸리티 코드를 정리한 레포지토리입니다.
본 대회는  특정 운동 동작을 수행하고 있는 사람의 미리 지정된 각 신체 부위의 위치에서 측정한 데이터를 활용하여 신체 동작 마다의 키포인트를 검출하는 대회입니다. 
자세한 자료는 링크를 들어가서 확인해 주세요.

### visualize_from_json.py
coco 데이터셋의 json annotation을 visualize 하는 코드입니다. 
### visualize_from_csv.py
데이콘 최총 제출물의 csv annotation을 visualize하는 코드입니다. 
### postprocessing_from_csv.py
팔과 발등의 좌표를 후처리하는 코드이빈다. 
### ensemble_from_submit_csv.py
결과물 csv 파일들을 앙상플 하는 코드입니다. 
### compare_csv.py
결과물 csv 파일들끼리 차이값을 계산해서 어느정도 차이가 생기는지 확인할 수 있는 코드입니다. 
### _utils.py
위의 유틸리티 코드들 중 중복되는 함수를 리스트업한 모듈입니다. 
