# __init__(self,초기파라미터1,초기파라미터2,...)
# 첫번쨰 파라미터로 반드시 self가 와야함)
class Person :
    # 객체 변수를 생성할 때 한번 호출됨
    def __init__(self,name='kate',age='23',sex='F'): # self 현재 클래스(person,모둘) 자기자신 지칭
        print(self,"is generated")
        # Person의 속성을 생성
        self.name= name # Person을 나타내는 속성/ 초기값
        self.age= age # Person을 나타내는 속성 / 초기값
        self.sex=sex



class Rectangle :
    # 객체 변수를 생성할 때 한번 호출됨
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def calc(self):
        print("계산합니다.")

#인스턴스 생성
t1=Person('Kim',25,'M')
t2=Person('Hong',30)
t3=Person()
print(t1.name)
print(t1.age)
print(t2.name)
print(t2.age)

print(t1.name,t1.age,t1.sex)
print(t2.name,t2.age,t2.sex)
print(t3.name,t3.age,t3.sex)

# Rectangle 인스턴스 생성
r1=Rectangle(3,4)
r2=Rectangle(10,2)
print(r1.width,r1.height)
print(r2.width,r2.height)
#test


