print("---------------전체라인 읽고 출력---------------")
f1=open("test.txt",'r')
lines=f1.readlines() #전체행 읽기
print(lines) #1개 행이 한개의 리스트 요소 행 끝에 \n이 포함되어 있음(엔터키 입력했기 떄문)
f1.close()


print("------------전체라인 읽고 한 행 씩 출력--------------")
f2=open('test.txt','r')
lines=f2.readlines()

for line in lines :
    print(line,end='')

f2.close()

print("\n------------readline()없이 파일 읽어오기----------------")
f3=open('test.txt','r')

for line in f3 : #f3.readline() 함수가 자동 수행되면서
    print(line,end='') #1행 씩 읽어옴
f3.close()