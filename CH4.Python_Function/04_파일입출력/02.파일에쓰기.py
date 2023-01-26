#쓰기모드로열고 파일 객체의 write()함수로 출력값을 파일에 기록
#f.write(데이터)
#open() - write() - close()
data="안녕하세요.ㅋㅋㅋ"
# f=open('file2.txt','w') encoding UTF-8로 다른이름으로 수동 저장
#한글파일은 encoding방식을 UTF-8로 쓰기
f=open('file2.txt','w',encoding='UTF-8')
f.write(data) #텍스트파일에 HI라는 문자열 쓰기
f.close() #닫기