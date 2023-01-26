from django.db import models

# Create your models here.
class Category(models.Model):
    # 테이블에 cartegory_name이라는 문자열을 저장할 컬럼을 추가하는 코드
    category_name=models.CharField(max_length=100)

class Restaurant(models.Model): # 맛집추가 DB
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT,default=6)
    restaurant_name = models.CharField(max_length=100) # 맛집 이릉
    restaurant_link = models.CharField(max_length=100) # 맛집 URL
    restaurant_content = models.TextField() # 맛집 설명
    restaurant_keyword = models.CharField(max_length=50)


