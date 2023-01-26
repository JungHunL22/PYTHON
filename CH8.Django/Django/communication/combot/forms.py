# combot>forms.py

from django import forms
from combot.models import Question,Answer

class QuestionForm(forms.ModelForm) :
    class Meta : # 장고 모델 폼은 Meta 클래스를 반드시 포함해야 한다.
        model = Question
        fields = ['subject','content']
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class':'form-control'}),
        #     'content': forms.Textarea(attrs={'class':'form-control','rows':10}),
        # }
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }

class AnswerForm(forms.ModelForm) :
    class Meta :
        model = Answer
        fields = ['content']
        labels = {
            'content':'답변내용',
        }






