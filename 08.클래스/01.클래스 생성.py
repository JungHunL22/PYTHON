# 인스턴스(클래스 객체 변수)를 생성하기 위해서는 모체가 되는 클래스를 정의
# class 클래스명 :
# 클래스 생성자
# 클래스 속성(변수,특성)
# 클래스 매서드(기능,함수)

# person 클래스 정의
# 빈클래스로 정의

class person :
    pass

# Rectangle 클래스 정의
# 속성과 매서드 포함
class Rectangle :
    count = 0 #클래스 속성
    def __init__(self): #클래스 생성자
        Rectangle.count+=1

    def print_count(self): #클래스 매서드
        print(self.count)

# print_count() 클래스 내부에 있는 함수기 떄문에 객체 인스턴스 생성 후 사용해야 함

#클래스 객체 인스턴스(객체변수) 생성
#변수명 = 클래스명([생성자매개변수])
rect1= Rectangle()
#객체 변수 rect1을 이용해 매서드 print_count()
rect1.print_count()
rect1.count

rect2 = Rectangle()
rect3 = Rectangle()
### 파이썬 내부 클래스 사용 예제
### 형변환 함수
a= '123'
#클래스 이름 int 클래스 생성자 함수 호출
int_a=int(a) #int_a는 int클래스의 인스턴스(객체변수)

b=123
#변수명=클래스명()
str_b=str(b)
str_b.replace('1','a') #str_b는 인스턴스(객체변수) ,replace 매서드