# models 클래스 : db와 관련된 최상위 클래스
# db를 테이블 형식으로 구성
# 앱에 필요한 db를 구성하기 위해서는 models.Model을 상속받아야 함
from django.db import models

# Create your models here.
class Todo(models.Model):
    # table을 구성
    # 테이블의 컬럼(필드)를 설정
    # 앱이름클래스명을 연결해서 테이블명을 만듦
    # my_to_do_app_todo 테이블이 생성됨
    # 생성된 테이블 정보 확인 : dbshell에서 PRAGMA table_info(my_to_do_app_todo)
    # 0열 ID / 1열 content
    # DB 테이블안에 저장된 행(레코드) 확인 : dbshell에서 select * from my_to_do_app_todo;
    # 행렬구조 ID,content라인이 보여짐
    content = models.CharField(max_length=255)
    # 변경된 사항(isDone열)을 업데이트? - python manage.py makemigrations
    # DB에 isDone열을 추가 -
    isDone=models.BooleanField(default=False) # 숨기기 버튼에 사용

    # DB안에 테이블 확인 - python manage.py migrate
    # python manage.py dbshell(dbshell에 접속)
    # .tables -> ;
