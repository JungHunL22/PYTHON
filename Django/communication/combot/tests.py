from django.test import TestCase

# Create your tests here.
class Question() :
    subject = "모델연습"

    def __str__(self):
        return self.subject

Q1 = Question()
# print(Q1.subject)
print(Q1)
