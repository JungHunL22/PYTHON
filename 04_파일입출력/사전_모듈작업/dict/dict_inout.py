from .dict_var import ek_dic #프로그램 실행중 사전 데이터를 갖고 있는 변수
#사전 읽어오기 저장하기 기능
def load_dict():
    #사전 파일은 초기에 빈파일을 하나 생성해 놓고 시작
     #읽어오기
    #저장을 한행에 한문장으로 저장하기 떄문에 리스트는 비어있거나 요소가 1개가 있음
    f=open('./res/eng_dict.txt','r',encoding='utf-8')
    results=f.readlines()
    #print(results)
    f.close()
    if results==[]:
        return 0

    # 키와 값 나누기
    res=results[0].split('-')
    d_keys=res[0].split(',')[:-1]
    d_values = res[1].split(',')[:-1]
    dict_temp=dict(zip(d_keys,d_values))
    #print(dict_temp)
    #ek_dic=dict_temp 지역변수로 지정되버림 전역변수로 지정해야함
    #ek_dic가 딕셔너리 이므로 아이템을 추가하는 방식으로 부분변경
    #공용변수에 dict_temp의 items들을 저장
    for item in list(dict_temp.items()):
        k,v=item
        ek_dic[k]=v


    print("사전 준비 완료!!!!")
def save_dict():
    #사전을 파일로 저장하는 함수
    result=''
    f=open('./res/eng_dict.txt','w',encoding='utf-8')
    #ek_dic의 키 - value 형태의 문자열 구성
    d_key=ek_dic.keys() #키만 추출
    d_value=ek_dic.values() #값만 추출
    #key를 문자열로 저장
    for k in d_key:
        result+=k+','
    #value와 구분자 추가
    result += '-'
    for v in d_value:
        result+=v+','
    #파일에 쓰기
    f.write(result)
    f.close()
    print("사전 저장 완료!!!!")
    #저장하기
