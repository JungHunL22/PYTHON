# my_to_do_app > views.py
# url 요청이 들어오면 응답하는 처리 함수 구성
from django.shortcuts import render
# request(요청)가 들어오면 HttpResponse를 임의로 만들어 강제 응답할 때 사용
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse # url 연결을 반대로 변경하는 함수
from .models import *
# Create your views here.
# 강제응답 함수
# request 변수는 클라이언트가 요청 시 전송한 모든 data를 받는 변수(사용자 입력값도 포함됨)
# def index(request):
    # http://127.0.0.1:8000 요청에 대응하는 응답 객체 반환
    # return HttpResponse("my_to_do_app 첫번째 페이지를 응답합니다!")

def index(request):
    # 사용자가 그동안 저장한 메모 index.html에 출력
    # db에 저장된 메모데이터 모두 추출 : 클래스명.objects.all() 함수사용
    # select * from my_to_do_app_todo;
    todos = Todo.objects.all()

    # rendering 할 수 있게 templates로 전달 : 딕셔너리로 전달
    contents = {'todos' : todos}

    # http://127.0.0.1:8000 요청에 대응하는 HTML 페이지 반환
    return render(request,'my_to_do_app/index.html',contents)
    # template는 경로지정 안해도 됨(같은폴더)
# def createTodo(request):
#     return HttpResponse("createTodo 작성합시다. 메모하기 버튼 눌렀어요.")

def createTodo(request):
    # 사용자가 메모 입력칸에 입력해서 전송된 내용을 응답
    # input 태그의 경우 name 속성의 값에 담아서 전달됨
    # input 태그의 속성 : name='todoContent',method='Post'
    # 변수 todoContent에 있는 값을 Post방식으로 추출
    # 클라이언트가 보낸 값은 request안에 다 들어 있음
    user_input_str = request.POST['todoContent']
    # DB에 저장하기 위한 모델객체
    new_todo = Todo(content=user_input_str)
    # DB 테이블내 컬럼 content에 저장
    # views와 models가 연결됨
    new_todo.save()
    # return HttpResponse('DB에 저장했습니다.=>'+user_input_str)
    # url pattern name이 index인 url 강제 요청
    return HttpResponseRedirect(reverse('index'))

def deleteTodo(request):
    # 클라이언트가 get방식으로 서버에 전송한 데이터 todoNum을 추출
    # input 태그의 속성 : name='todoNum',method='Post'
    done_todo_id = request.GET['todoNum']
    print('완료를 누른 todo의 id',done_todo_id)
    # 삭제하려는 레코드의 객체변수 반환 : 클래스.objects.get(조건)
    # select * from my_to_do_app_todo where id=1;는 아래코드와 같은 뜻
    todo=Todo.objects.get(id=done_todo_id)
    # 삭제명령 : 레코드객체변수.delete
    # todo.delete()
    # 삭제 대신 숨기기(DB에는 저장되어 있는 상태로 화면에만 출력하지 않음)
    todo.isDone=True # 화면에 보여질지 말지 결정하는 컬럼에 True를 대입
    todo.save() # 위에서 대입한 True를 save
    return HttpResponseRedirect(reverse('index'))
        #HttpResponse('DB에서 삭제 예정입니다.. =>'+done_todo_id)