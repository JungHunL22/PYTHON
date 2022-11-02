# 클래스라는 개념을 만들어 낼 때 반드시 필요하다고 약속된 특수 함수

# 개발자가 안만들면 번역기가 무조건 정의함

# 파이썬에서 생성자 함수를 만들기 위해서

# __init__(self) 생성자

class Person :
    # 객체 변수를 생성할 때 한번 호출됨
    def __init__(self): # self 현재 클래스(person,모둘) 자기자신 지칭
        #print(self,"is generated")
        # Person의 속성을 생성
        self.name='Kate' # Person을 나타내는 속성/ 초기값
        self.age=10 # Person을 나타내는 속성 / 초기값

    def __str__(self):
        return '{},{}'.format(self.name,self.age)

p1=Person()
print(p1)

class Rectangle :
    # 객체 변수를 생성할 때 한번 호출됨
    def __init__(self):
        self.width=1
        self.height=1


# #생성자 함수를 호출하는 방법 : 객체 변수를 할당
# p1 = Person() # p1 객체변수 생성자 함수 호출
# p2 = Person() # p2 객체변수 생성자 함수 호출
#
# print(p1.name) #p1이 사용할 수 있는 변수 name을 생성했음
# print(p2.name) #p1이 사용할 수 있는 변수 name을 생성했음
#
# p1.name='hong' # p1만의 공간을 할당했으므로 name을 변경가능
# print(p1.name)
#
# p2.name='lee' # p2만의 공간을 할당했으므로 name을 변경가능
# print(p2.name)
#
# p2.age=36
# p1.age=25
#
# r1=Rectangle()
# r2=Rectangle()
# print(r1.width)
# print(r1.height)
#
# r1.width=10
# r1.height=20
# print(r1.width)
# print(r1.height)
#
# r2.width=100
# r2.height=30
# print(r2.width)
# print(r2.height)
