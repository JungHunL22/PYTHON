#dict_var.py가 동일한 경로에 존재해서 패키지명 호출안해도됨
#ModuleNotFoundError: No module named 'dict_var'함수호출 기준위치 변경
#실행은 되지만 코드 변경
#from dict.dict_var import ek_dic
#.모듈은 기준위치를 해당모듈파일이 있는 위치가 기준위치가 됨
#기준위치를 바꿔주지 않으면 영단어 사전 함수화.py가 기준위치이므로 에러
#ModuleNotFoundError: No module named 'dict_var'
from .dict_var import ek_dic
#사전 단어 등록 관련 함수
###################################################
def input_dict(eng):
    #단어에 해당하는 뜻 입력
    kor=input(eng+"뜻 입력 : ")
    ek_dic[eng]=kor
    #반환값 필요 없고 출력값도 필요 없음

#2. 사용자로부터 단어를 입력받아 사전에 단어가 있는지 검색 후
#사용자로부터 단어를 입력 받아 사전에 단어가 있는지 검색
#단어가 없으면 input_dict(eng)함수 호출해서 뜻을 저장
#단 사전등록은 사용자가 원하는 만큼 등록이 가능하게 할 것이므로 무한루프 사용

def const_dict():
    while True :
        #영어단어 입력받기
        eng=input("\n영어 단어 입력 (종료는 'q') : ")
        #종료검사
        if eng =='q':
            print('단어 등록을 종료합니다.')
            break #반복종료 (반복 외에 함수에 다른 문장없으므로 함수 종료)
        elif eng not in ek_dic : #등록되지 않은 단어
            input_dict(eng)
        else :
            print("%s는 이미 등록된 단어 입니다." %eng)