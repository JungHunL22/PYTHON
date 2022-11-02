import mypack.pack1.module11
#사용 시 패키지.모듈.함수명()
mypack.pack1.module11.function11()

#패키지 모듈명이 길 경우 별칭을 사용할 수 있다.
import mypack.pack1.module11 as mm1
mm1.function11()

#from 패키지.패키지.모듈 import 함수
from mypack.pack2.module21 import function21
function21()

#사용 시 함수명()
from mypack.pack2.module21 import *

#패키지.모듈.함수는 불가능
#from도 패키지.모듈.함수는 불가능 from 패키지.모듈 impoert 함수로 호출해야함