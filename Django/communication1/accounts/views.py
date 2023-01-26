from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from accounts.forms import Userform

# Create your views here.
def signup(request):
    if request.method=="POST":
        form = Userform(request.POST)
        if form.is_valid():
            # 넘어온 데이터 저장
            form.save()
            # user_name, password1을 추출
            user_name= form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user = authenticate(username=user_name,password=raw_password)
            login(request,user)
            # 로그인 진행
            return redirect('main')
    else:
        form = Userform()
    return render(request,'accounts/signup.html',{'form':form})