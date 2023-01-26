money=10000
a=0
while money>0:
    money-=2000
    a+=1
    print("노래를 %d곡 불렀습니다."%a)
    if money>0:
        print("현재 %d원 남았습니다."%money)
    else :
        print("잔액이 없습니다. 종료합니다.")