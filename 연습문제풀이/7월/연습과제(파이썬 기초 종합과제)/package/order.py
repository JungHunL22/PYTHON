# 주문 목록 가격 리스트 생성
def order(total,a):
    total.append(a)
    return sum(total)

# 거스름돈 계산
def change(x,y):
    total=x-y
    if total<0:
        print('지불하신 금액은 %d 원 입니다.' %x)
        print('주문하신 음식은 총 %d 원 입니다.' %y)
        print("지불하신 금액이 %d원 모자랍니다. "%abs(total))
    else:
        print('지불하신 금액은 %d 원 입니다.' %x)
        print('주문하신 음식은 총 %d 원 입니다.' %y)
        print('거스름돈은 %d 원 입니다.' % total)

