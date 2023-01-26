# accounts > urls.py
from django.urls import path
# 장고가 제공하는 계정과 관련된 view import
from django.contrib.auth import views as auth_views
from . import views
app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/', views.signup, name='signup')
]