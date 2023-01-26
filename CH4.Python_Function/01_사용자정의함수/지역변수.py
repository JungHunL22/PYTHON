def show():#a는 지역변수
    a=1
    a=a+1
    print(a)

show()
#a가 지역변수이므로 에러

#함수정의2
def show2(b): #b는 지역변수
    b+=1
    print(b)

show2(10)
print(b)
#b가 지역변수이므로 에러