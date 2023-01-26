goods=['노트북','디지털카메라']
price=[1200000,400000]
print("*************상품 정보****************")
print('1 :',goods[0]," : "+format(price[0],','))
print('2 :',goods[1]," : "+format(price[1],','))
print("************************************")
num=int(input("상품번호 입력 : "))
quan=int(input("주문 수량 입력 : "))
order=quan*price[num-1]
if not(num==1 or num==2):
    print("잘못 입력하였습니다. 종료합니다.")
else:
    if order>=1000000:
        dc=int(order*0.1)
    elif order<1000000 and order>=500000 :
        dc=int(order*0.05)
    else:
        dc=0
    total=order-dc
    print("\n***************주문 내용*****************")
    print("상품명 : \t", goods[num-1])
    print("가  격 : \t",format(price[num-1], ','), " 원")
    print("주문 수량 : \t",quan)
    print("주문액 : \t",format(order,','))
    print("할인액 : \t",format(dc,',')," 원")
    print("총지불액 : \t",format(total, ','), " 원")
