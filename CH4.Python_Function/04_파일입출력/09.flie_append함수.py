#파일끝에 내용 추가
#열기모드 a
f=open('test2.txt','a',encoding='utf-8')
a_data="\n\nPython programing"
f.write(a_data) #파일 끝에 데이터 추가

#읽기모드로 바꿔서 다시 파일 열고 출력
f=open("test2.txt",'r',encoding='utf-8')
print(f.read())
f.close()