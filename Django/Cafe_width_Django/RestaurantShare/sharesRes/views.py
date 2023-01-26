from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.


# def index(request):
#     return HttpResponse("메인페이지를 호출했습니다.")
def index(request):
    categories = Category.objects.all() # select * from category;
    restaurants = Restaurant.objects.all() # select * from restaurant;
    # rendering하기 위한 딕셔너리로 구성
    content = {'categories': categories,'restaurants':restaurants}
    return render(request,'sharesRes/index.html',content)

def restaurantDetail(request,res_id):
    # res_id는 url에 포함되어 전달되는 맛집 id/ url패턴 설정 시 추가해준 arg이기 때문에
    # 반드시 처리 함수에서 파라미터로 받아줘야 함

    # res_id에 해당하는 맛집 정보를 DB에서 추출
    rest = Restaurant.objects.get(id=res_id)
    content = {'rests':rest}
    return render(request,'sharesRes/restaurantDetail.html',content)

def restaurantCreate(request):
    categories = Category.objects.all()
    content = {'categories' : categories}
    return render(request,'sharesRes/restaurantCreate.html',content)

def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories' : categories}
    return render(request,'sharesRes/categoryCreate.html',content)

def Create_category(request): # 카테고리 새로 추가하는 함수(reverse)
    category_name = request.POST['categoryName']
    # DB table에 저장하기 위해서 모델객체 생성
    new_category=Category(category_name=category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))

def Delete_category(request):
    category_id = request.POST['categoryId'] # hidden 태그로 전송됨
    del_cate = Category.objects.get(id=category_id)
    del_cate.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))

def Create_restaurant(request): # 카테고리 새로 추가하는 함수(reverse)
    # 맛집 정보를 추출해 DB에 저장
    # 맛집 추가에 사용자가 입력한 정보를 추출
    category_id = request.POST['resCategory']
    # 해당 category_id가 있는지 확인 추출
    # id가 없어서 none이 반환되면 기본 id로 저장됨
    category = Category.objects.get(id=category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    # 저장을 위한 모델 객체 생성
    new_res = Restaurant(category=category,
                         restaurant_name=name,
                         restaurant_link=link,
                         restaurant_content=content,
                         restaurant_keyword=keyword)
    # DB저장
    new_res.save()
    # 기본 index 페이지로 reverse
    return HttpResponseRedirect(reverse('index'))

def restaurantUpdate(request,res_id):
    categories = Category.objects.all() # 카테고리 테이블의 모든 레코드 추출
    rest = Restaurant.objects.get(id=res_id)
    content = {'categories' : categories,'rests':rest}
    return render(request,'sharesRes/restaurantUpdate.html',content)

def Update_restaurant(request):
    return HttpResponse('맛집 수정')