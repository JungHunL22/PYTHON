#파일 내에 입력된 문자가 있는지 확인하는 예제
#read() 사용
f=open('test2.txt','r',encoding='utf-8')
data=f.read() #파일내용을 하나의 문자열로 읽어옴
f.close()
value=input("검색 값 입력 : ")
#문자열의 검색값이 있는 지 확인
if value in data:
    print("있음")
else:
    print("없음")

