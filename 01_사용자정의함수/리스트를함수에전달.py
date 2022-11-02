#리스트를 함수에 인수로 전달 시 알아야 할 사항
#함수정의
def show_list(my_list1):
    print("함수내부 출력1", my_list1) #지역변수 my_list
    print("매개변수 my_list의 id : ", id(my_list1))
    my_list[0]=10 #my_list의 첫번째요소 부분 변경
    print("함수내부 출력2", my_list1) #10,2,3,4달
#호출테스트
my_list=[1,2,3,4] #리스트생성
print("출력1", my_list)
show_list(my_list) #리스트를 인수로 전달
print("출력2", my_list) #전역변수 my_list 출력
#함수 내부에서 변경시킨 값이 외부에도 반영
# (주소로 변경해서 값 자체가 변경)
print("전역변수 my_list의 id : ", id(my_list))