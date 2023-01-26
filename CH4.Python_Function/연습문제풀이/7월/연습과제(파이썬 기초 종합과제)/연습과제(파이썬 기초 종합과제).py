# 필요한 함수 호출
from package.menu import *
from package.order import *
# 메뉴 불러오기
food=menu()
# 주문가격 저장
price=list()
# 주문 시작
while True:
    product = input('무엇을 주문하시겠습니까? ')
    # 주문할 음식이 있는 경우
    if product in food.keys():
        print('가격 : %s 원 입니다.'%food[product])
        totalp=order(price,int(food[product]))

    # 주문할 음식이 없을 경우
    elif product=='x':
        # 지불 받은 돈(주문한 음식이 있을 때만 돈 지불)
        if len(price) > 0:
            money = int(input('지불하신 금액 : '))
            # 받은돈, 메뉴총합, 거스름돈 계산
            change(money, totalp)

        # 아무것도 주문하지 않은 경우
        else:
            print("주문 받은 음식이 없습니다.")
        break

    # 메뉴에 없는 음식일 경우
    else:
        print('메뉴에 없는 음식입니다.')




