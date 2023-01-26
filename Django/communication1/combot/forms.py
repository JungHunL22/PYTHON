from django import forms
#from combot.models import Question,Answer

class QustionForm(forms.modelForm):
    class Meta :
        model = Question
        fields = ['subject','content']
        labels = {
            'subject':'제목',
            'content':'내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta :
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변내용',
        }