class Person :
    # 객체 변수를 생성할 때 한번 호출됨
    def __init__(self,name='kate',age='23',sex='F'): # self 현재 클래스(person,모둘) 자기자신 지칭
        print("self : ", self)
        # Person의 속성을 생성
        self.name= name # Person을 나타내는 속성/ 초기값
        self.age= age # Person을 나타내는 속성 / 초기값
        self.sex=sex
    def sleep(self): #파라미터가 한개 있는 메서드. 단, 첫번쨰 파라미터는 클래스의 참조값
        print("self : ", self)
        print(self.name,'은 잠을 잡니다.')


class Rectangle :
    # 객체 변수를 생성할 때 한번 호출됨
    def __init__(self,width,height):
        print('self : ',self)
        self.width=width
        self.height=height
    def calcArea(self):
        area = self.width * self.height
        return area

#############################################
a=Person('Aaron',20,'M')
b=Person("Bob",30)

print(a)
print(b)

a.sleep()
b.sleep()

#Rectangle() 사용
r_a=Rectangle(10,30)
r_b=Rectangle(3.5,2.1)
print("면적 r_a : ",r_a.calcArea())
print("면적 r_b : ",r_b.calcArea())