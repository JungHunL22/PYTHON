#17 리스트를 함수에 전달
def show_list(my_list):
    print("함수 내부에서 출력 1 : ",my_list)
    my_list[0]=10 #리스트 부분변경
    print("함수 내부에서 출력 2(부분변경) : ",my_list)
    print("함수 내부 출력, id : ",id(my_list))
#함수 내에서 매개변수 my_list의 전체 요소값을 변경
    my_list=[100,200,300]
    print("함수 내부 출력3(전체변경), id : ", id(my_list))
    #원본 리스트전체 새로값 저장시
    #전체변경이아닌 새로운 리스트를 생성
    #새로운 리스트인 [100,200,300]을 생성하는 것임
    print("함수 내부에서 출력2 : ",my_list)
my_list=[1,2,3,4]
print("함수 외부에서 출력 1 : ",my_list)
show_list(my_list)
print("함수 외부에서 출력 2 : ",my_list)
print("함수 외부 출력, id : ",id(my_list))