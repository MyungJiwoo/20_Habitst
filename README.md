#HABITST#
[LIKELION_HACKATHON] 취미 공유 사이트 HABITST

HABITST 서비스란?
자신의 취미를 블로그 형식으로 공유하고, 더 나아가 비슷한 취미를 가지고 있는 사람들과 함께 모임을 생성해, 취미를 즐길 수 있는 웹 페이지 입니다.

#주요 서비스 소개#
>main
메인 페이지에는 최신순, 좋아요가 가장많은 순으로 글을 볼 수 있습니다.

>mypage
개인정보(회원 가입할 때 기입한 것)
내가 쓴 글
자기소개 페이지 - 왼쪽 상단에 자기 프로필 사진이랑 사진 밑에 간단한 자기소개 보여지기.
>withme
모임을 주최한 사람 정보
모임 장소 & 시간
모임에 대한 소개
기타 내용
사진첨부
>postblog
작성자
작성일
제목/내용/이미지/글
조회수/좋아요수
>Login/Signup
Customuser 사용
Social Login
>withmepayment
Iamport 사용(결제 api)
redis-server 적용(채팅)
실행방법 :

redis설치 및 (필수)
pip install django-allauth
pip install django-crispy-forms
pip install django-summernote
pip install iamport-rest-client
pip install django_social_share
python -m pip install -U channels
pip install channels_redis
python -m pip install Pillow
python manage.py runserver
runserver시 no module에 관한 부분은 pip install django_xxxxxx형태로 설치
배포버전 문의 : 01081916245
