from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

# Question 입장에서는 Answer가 ForeignKey로 연결되어 있으므로
# 장고는 Question 객체 메서드로 oreignKey로 연결된 클래스명_set.create()를 제공
# 클래스명은 전부 소문자여야 함
# 이 메서드의 기능은 ForeignKey로 연결된 클래스(table)에 레코드(행)저장을 가능하게 한다.

class Answer(models.Model) :
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()