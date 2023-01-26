# combot > urls.py
from django.urls import path,include
from . import views

app_name = 'combot' #네임스페이스 등록

urlpatterns = [
    # '' : http://localhost:8000/combot/
    path('', views.index,name='index'),
    # http://127.0.0.1:8000/combot/3 : 3은 질문 번호(args)
    path('<int:question_id>', views.detail, name='detail'),
    path('answer/crate/<int:question_id>', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]