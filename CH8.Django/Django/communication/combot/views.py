from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator #리스트(게시판등) 페이징 기능을 구현하는 함수
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request) :

    # 현재 페이지 설정하기 : request 객체를 통해서 설정 가능
    page = request.GET.get('page','1')
    # 질문 리스트 추출(DB에서)
    question_list = Question.objects.order_by('-create_date')

    # 페이징 처리
    # 페이지 객체 생성 : Paginator(페이징처리할data, 한페이지 게시물 수)
    paginate = Paginator(question_list,10) # 페이지당 10개씩
    page_obj = paginate.get_page(page) # 한 페이지에 10개씩 분할된 리스트들의 집합이 반환

    context = {'question_list':page_obj}
    return render(request, 'combot/question_list.html',context)

def detail(request,question_id) :
    # question = Question.objects.get(id=question_id) # 오류 발생시 db 오류 발생
    question = get_object_or_404(Question, pk=question_id) # 오류 발생시 404 오류 발생
    context = {'question':question}
    return render(request, 'combot/question_detail.html',context)

@login_required(login_url='accounts:login')
def answer_create(request, question_id) :
    # answer에 저장할 question 객체 생성
    # question은 answer의 ForeignKey로 연결되어 있음
    # question = get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'),
    #                            create_date= timezone.now())

    # 요청이 get/post 냐에 따라 다른 응답을 하도록 구성
    question = get_object_or_404(Question, pk=question_id)
    # 요청이 POST 방식으로 들어오면
    if request.method == "POST" :
        # POST 방식으로 전달된 데이터를 포함하는 폼 생성
        form = AnswerForm(request.POST)
        # 전달된 폼 데이터가 유효하면
        if form.is_valid() :
            # db에 data 저장
            answer = form.save(commit=False) # form객체를 통해 전달된 데이터 db저장 준지
            answer.author = request.user  # 추가한 author 속성에 로그인된 사용자 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            # 질문 상세보기 페이지로 이동
            return redirect('combot:detail',question_id=question.id)
    else : # 요청이 GET 방식으로 들어오면
        # 빈 폼을 생성
        form = AnswerForm()
    context = {'question':question,'form':form}
    return render(request, 'combot/question_detail.html', context)

# 장고 폼 기능 사용 연습
def question_create(request) :
    # 요청이 POST 방식으로 들어오면 사용자가 전송한 값을 db에 저장 후 list 화면으로 redirect
    if request.method == 'POST' :
        # form 객체 생성
        form = QuestionForm(request.POST)
        if form.is_valid(): #위에서 생성한 request data 담고 있는 폼객체가 정상인지 확인
            question = form.save(commit=False)
            question.author = request.user  # 추가한 author 속성에 로그인된 사용자 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('/combot')
    else :
    # 요청이 GET 방식으로 들어오면 질문 입력 FORM을 클라이언트에게 전달
        # 질문 등록 Form 작성 코드
        form = QuestionForm() # 사용자 정의 Form class 명
    return render(request, 'combot/question_form.html',{'form':form})










