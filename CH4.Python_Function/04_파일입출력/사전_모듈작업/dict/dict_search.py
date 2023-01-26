#dict_var.py가 동일한 경로에 존재해서 패키지명 호출안해도됨
#실행되지만 다른 코드로 변경
#from dict.dict_var import ek_dic
#from dict.dict_const import input_dict
#.모듈은 기준위치를 해당모듈파일이 있는 위치가 기준위치가 됨
from .dict_var import ek_dic
from .dict_const import input_dict

#검색기능
#1. 단어를 전달받아 뜻을 검색 후 출력하는 함수 :dict_search(eng)
def dict_search(eng) : #단어가 사전에 있는 경우 호출
    print("%s의 뜻은 %s입니다. " %(eng,ek_dic[eng]))
#2. 단어 하나를 검색하는 함수
#단어 하나를 입력받아 입력 단어가 사전에 있으면 dict_search(eng)를 호출해서 뜻을 출력
#입력 단어가 사전에 없으면 사전에 등록할 것인지 여부 확인
#등록하겠다고 하면 input_dict(eng) 호출, 사전에 단어를 등록
def search() :
    #검색단어부터 입력받기
    eng=input("\n 검색할 단어 입력 : ")
    if eng in ek_dic : #사전에 있는 단어라면
        dict_search(eng)
    else : #사전에 없는 단어라면
        print("%s는 사전에 없는 단어 입니다." %eng)
        answer=input('사전에 등록 하시겠습니까?(Y/N)')
        if answer=='Y':
            input_dict(eng)
            print("사전 등록완료! 감사합니다!")
    print("검색을 종료합니다.")
