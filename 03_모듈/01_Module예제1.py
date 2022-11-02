#생성해놓은 모듈 import
import calculator #현재파일과 같은 디렉터리
a= calculator.add(7, 4)
print(a) #모듈명.함수명(인수)
#* : 모든함수 사용
from calculator import *
s=sub(2,7)
print(s)

m=mul(7,4)
print(m)

d=int(div(6,3))
print(d)