with open("test3.txt",'w') as f:
    f.write('hello')
#with를 사용했기 떄문에 close()는 따로 사용하지 않아도 자동 종료
#파일명은 변수 사용 할 수 있음
flie="test4.txt"
data='''Python programing
R programing
web programing'''
with open(flie,'w') as f:
    f.write(data)