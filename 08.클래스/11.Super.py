# super : 부모클래스의 메서드를 가져와서 호춣
# 부모 클래스
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print('{}은 {}를 먹습니다.'.format(self.name, food))

    def sleep(self, minute):
        print('{}은 {}분동안 잡니다.'.format(self.name, minute))

    def work(self, minute):
        print('{}은 {}분 동안 준비를 합니다.'.format(self.name, minute))


# 자식 클래스인 Student와 Employee를 생성(Person 클래스 상속)
# 생성자 함수는 다시 선언해서 각 클래스의 속성을 재구성

# Person클래스 상속받아 Student 클래스 생성
# 상속 형식
# class 자식클래스명(부모클래스명) :
class Student(Person):
    # Student속성 name과 age를 재구성
    # 생성자함수 이용
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def work(self,minute): # 메서드 오버라이드
        # 부모클래스의 work메서드를 호출
        super().work(minute) # {}은 {}분 동안 준비를 합니다.
        print("{}은 {}분 동안 공부합니다.".format(self.name,minute))

class Employee(Person):
    # Employee 속성 name과 age를 재구성
    # 생성자함수 이용
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def work(self,minute): # 메서드 오버라이드
        super().work(minute) # {}은 {}분 동안 준비를 합니다.
        print("{}은 {}분 동안 근무합니다.".format(self.name,minute))

e1=Employee('고길동',40)
e1.work(50)
# minute가 Person클래스의 work메서드의 인자로 전달된 후 호출
# 그 이후 Employee클래스의 work메서드를 호출

s1=Student('둘리',15)
s1.work(30)
# minute가 Person클래스의 work메서드의 인자로 전달된 후 호출
# 그 이후 Employee클래스의 work메서드를 호출