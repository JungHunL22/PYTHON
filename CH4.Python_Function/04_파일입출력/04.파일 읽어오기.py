#readline() 함수를 이용해 1개라인 읽어오기
print("----------------첫번째 행 읽기---------------------")
f1=open('test.txt','r') #읽기모드 - txt파일이기 떄문에 파이썬 내부에서 한글처리 진행
#f1=open('test.txt','r',encoding='utf-8') 한글이 깨지는 경우 encoding변경
line=f1.readline() #첫번째 라인 읽기
print(line)


print("----------------파일 전체 읽기---------------------")
f2=open('test.txt','r')
#해당파일의 총 라인수를 알 수 없으므로 무한반복 루프
while True:
    line2=f2.readline()
    if not line2: #라인에 읽은내용이 없으면
        break
    print(line2,end='') #end=''로 print문 자체의 줄바꿈은 하지 않음
    # (원본에 엔터키를 쳤으므로)
f2.close()