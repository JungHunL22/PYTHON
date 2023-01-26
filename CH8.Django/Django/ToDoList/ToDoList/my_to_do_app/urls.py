# my_to_do_app > urls.py

from django.urls import path
# 같은 디렉터리 내에 views를 호출해서 찾아줌
from . import views
urlpatterns = [
    # http://127.0.0.1:8000 요청이 넘어오면 views.py파일에 index 함수가 응답(호출)
    path('',views.index,name='index'),
    # include 경로를 타고 들어와서 createTodo를 이 파일에서 찾음
    # http://127.0.0.1:8000/createTodo/ 요청이 넘어오면
    # views.py파일에 createTodo 함수 응답
    path('createTodo/',views.createTodo,name='createTodo'),
    # http://127.0.0.1:8000/deleteTodo/ 요청이 넘어오면
    # views.py파일에 deleteTodo 함수 응답
    path('deleteTodo/',views.deleteTodo,name='doneTodo'),
]