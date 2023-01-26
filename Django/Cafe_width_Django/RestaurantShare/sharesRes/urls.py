# sharesRes > urls.py

from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
# http://127.0.0.1:8000/restaurantDetail/
    path('restaurantDetail/<str:res_id>',views.restaurantDetail,name='resDetailPage'),

    # http://127.0.0.1:8000/restaurantDetail/updatePage/update
    path('restaurantDetail/updatePage/update', views.Update_restaurant, name='resUpdate'),

    # http://127.0.0.1:8000/restaurantDetail/updatePage/1
    path('restaurantDetail/updatePage/<str:res_id>',views.restaurantUpdate,name='resUpdatePage'),


    # http://127.0.0.1:8000/restaurantCreate/
    path('restaurantCreate/', views.restaurantCreate, name='resCreatePage'),
    # http://127.0.0.1:8000/restaurantCreate/create
    path('restaurantCreate/create', views.Create_restaurant, name='rescreate'),

    # http://127.0.0.1:8000/categoryCreate/
    path('categoryCreate/',views.categoryCreate,name='cateCreatePage'),


    # http://127.0.0.1:8000/categoryCreate/create
    path('categoryCreate/create',views.Create_category,name='cateCreate'),
    # http://127.0.0.1:8000/categoryCreate/delete
    path('categoryCreate/delete',views.Delete_category,name='cateDelete'),


]

# index 함수를 구성 : http://127.0.0.1:8000을 호출하면
# 1. "메인페이지를 호출했습니다." 가 클라이언트로 전송되게 코딩
# 2. 위에서 작성한 코드를 주석처리하고 index.html 파일이 클라이언트에게 전송되게 코딩