#영어사전 프로그램 -모듈화

#사전 생성 함수 : 단어를 사전에 등록하는 기능
#1. 단어를 전달 받아 사전에 단어 등록 : input_dict(eng)
#2. 등록 전 단어 필터림 : const_dict()

#사전 검색 모듈 : 등록된 사전을 이용해 검색기능
#dict_search.py


#사전 검색 함수
#1. 단어를 전달받아 뜻을 검색 후 출력하는 함수 : dict_search(eng)
#2. 검색하려는 단어를 입력받아 사전에 있는 지 필터링 : search()

#공용 사용 변수 모듈
#dict_var.py

#사전 사용 메뉴 프로그램
#######################
#단어가 저장될 dict 구성
#######################

#모듈 호출
#######################################################


from dict.dict_search import * #dict패키지의 dict_search모듈의 모든함수 호출
from dict.dict_const import * #dict패키지의 dict_const모듈의 모든함수 호출
from dict.dict_inout import *

#영어사전을 파일에서 읽어오고 저장하는 기능 추가
# dict_inout()
#사전프로그램을 실행시키면 사전을 읽어와서 준비
# load_dict()
#파일을 읽어옴 dog,cat,-강아지,고양이,
#split()함수로 분리 후 딕셔너리 구성
#사전프로그램을 종료시키면 ek_dic내의 item을 파일로 저장
# save_dict()
#ex 'dog':'강아지','cat':'고양이'와 같은 키형태를
#dog,cat,-강아지,고양이로 저장

###################################################
#메뉴 : 사전 프로그램은 사용자가 종료를 선택하면 완전 종료
load_dict() #사전에서 파일 내용 읽어오기
while True :
    print("===================메 뉴=====================")
    print("1. 사전 등록 : ")
    print("2. 사전 검색 : ")
    print("3. 종 료 : ")
    sel=input("사용할 메뉴를 선택하세요. 1/2/3/ : ")
    if sel=='1':
        print("사전에 단어를 등록합니다. 원하는 단어 수 만큼 등록이 가능합니다.")
        const_dict()
        #함수만 호출할 경우, 영단어 사전 함수화가 기준경로이므로 에러가 뜸
        #ModuleNotFoundError: No module named 'dict_var'
        #print(ek_dic) 내용 확인용
    elif sel=='2':
        print("단어 1개에 대하여 사전 검색을 시작합니다.")
        search() #사전 검색 전 필터링 함수
    else :
        print("사전 프로그램을 종료합니다.")
        save_dict()
        break