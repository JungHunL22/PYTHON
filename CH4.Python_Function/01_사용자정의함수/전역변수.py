#전역변수
#함수 외부에서 정의된 변수
#프로그램 내 모든 곳에서 사용가능
#함수 내에서 전역변수 값을 변경하려면 globl사용

a=1 #전역변수 a
def add():
        c=a+b #지역변수 c 전역변수 b
        print("add()에서 출력")
        print(a)
        print(b)
        print(c)


def show():
    print("show()에서 출력")
    print(a)
    print(b)

b=2

#함수 호출
add()
show()

#함수 외부에서 전역변수 사용
print("함수 외부에서 출력 :")
print(a)
print(b)

#함수정의(전역변수 함수 내에서 변경)
def add1():
    a=10 #지역변수
    a=a+1
    c=a+b #a,b가 전역변수,c는 지역변수
    print("add()에서 출력")
    print(a)
    print(b)
    print(c)

def add2():
    global a #전역변수
    a=a+1 #전역변수 a를 1증가시킴
    c=a+b #a,b가 전역변수,c는 지역변수
    print("add()에서 출력")
    print(a)
    print(b)
    print(c)
    print(d)

add1()
add2()
#함수 호출 후에 전역변수d를  생성해서 d변수를 인지하지 못해 에러
d=10
print(a)