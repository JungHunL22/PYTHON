#절댓값 abs
print(abs(-10))
#리스트 등의 모든 요소가 참이면 true, 아니면 false반환 all
#all(iterable)
#false : 0 true : 0을 제외한 모든 값
#즉, 0이 하나라도 있으면 false 반환
#iterable : 반복가능한 자료형, 각각의 요소를 하나씩 반환할 수 있는 형태
#for문으로 반복이 가능한 자료형 : 리스트, 튜플, 딕셔너리, 집합
print(all([1,2,3]))
print(all([0,1,2,3]))
#리스트 등의 요소가 하나라도 참이면 true, 아니면 false반환 all
#any(iterable)
print('-----------------------any()--------------------------')
print(any([0,0,0])) #false
print(any([0,1,2,3])) #true
print(any([0,"",[]])) #false 빈문자열,빈리스트는 false
print(any([None,None])) #false (0이 아닌 모든 값과 문자열은 false)
print('-----------------------chr()--------------------------')
print(chr(97)) #a
print(chr(65)) #A
print(chr(13)) #enter

print('-----------------------ord()--------------------------')
print(ord('a'))
print(ord('0'))
print(ord('\n')) #10(엔터가아닌 new line)
print(ord(' '))
print(ord('\r')) #13 : enter

print('-----------------------div()--------------------------')
#divmod(a,b) a를 b로 나눈 몫과 나머지를 튜플 형태로 반환
print(divmod(7,3))

print('-----------------------enumerate()--------------------------')
#enumerate(iterable,start=0)
#인덱스 값을 포함하는 객체로 반환

print(enumerate(['kim','lee','park']))
for name in enumerate(['kim','lee','park'],start=2):
    print(name)

for i,name in enumerate(['kim','lee','park'],start=3):
    print(i,name)
#for문 처럼 반복되는 구간에서 객체가 어느 위치에 있는지 인덱스 값이 필요할 때 유용
for index,value in enumerate(['Kim','Lee','Park']):
    print(index,value)


print('-----------------------filter()--------------------------')
#반복 가능한 자료형 요소들이 함수에 입력되었을 때 반환값이 참인 것만 묶어서
#실습위한 함수 정의
def positive(x) :
    return x>0 #True/False로 반환/양수만 반환
print(filter(positive,[0,-1,5,-7,10]))
print(list(filter(positive,[0,-1,5,-7,10])))

def even_n(x):
    if x%2==0:
        return x
#1,2,3,4,5,6,7,8(인자들을 한번씩 넘겨가며 True인 것만 반환)
print(list(filter(even_n,[1,2,3,4,5,6,7,8])))

print('-----------------------hex()--------------------------')
x=0x569F #16진수 값 저장
#정수 0x 접도사가 붙은 소문자 16진수 문자열로 변환
print(hex(7)) #0x7
print(type(hex(7))) #문자열로 반환
print(hex(10))
print(hex(1234))

print("\n----map----")
#iterable 각요소가 함수에 전달해서 수행된 결과를 반환
def increase(x):
    return x+1

print(list(map(increase,[1,2,3,4,5])))

#map,enumerate,zip 매우 중요

print("\n-----open-----")
#파일 입출력과 관계있는 함수
#open(filename,[mode]) : mode형식으로 파일열기
#mode(읽기방법)
#w 쓰기/ r 읽기 / a 추가 / b 이미지파일 등 모드
#현재디렉터리에 'my_file.txt를 쓰기모드로 생성
file_write=open('my_file.txt', 'w')

print("\n----pow()----")
#제곱
print(pow(2,3))

print("\n----round()----")
print(round(3.141592,3))

print("\n----sum()----")
print(sum([1,2,3,4,5]))
print(sum([3,5,7,9]))

print("\n----zip----")

#zip 각 iterable에서 동일한 인덱스의 요소를 추출하여 묶어서 반환
#zip 객체로 반환하고 내부에 iterable자료형으로 구성되어 있으므로 형 변환해 사용
print(list(zip([1,2,3,5],[4,5,6,11],[7,8,9,10])))
print(list(zip([1,2,3],[4,5,6])))
print(list(zip("123","abc")))
#zip함수를 이용해 튜플로부터 딕셔너리 생성
keys=('apple','pear','peach')
vals=(300,250,400)
print(tuple(zip(keys,vals)))
result=dict(zip(keys,vals))
print(result)

print("\n----lambda()----")
#람다식
#람사 : 실행시 생성해서 사용할 수 있는 익명 함수
#같은 함수를 def문으로 정의할 때 보다 간결
#형식 람다

def add(a,b):
    return a+b
print(add(3,5))

#일회성 함수 람다식으로 표현
print((lambda a,b:a%b)(6,2))

lambda_add=lambda x,y : x+y
print(lambda_add(3,5))