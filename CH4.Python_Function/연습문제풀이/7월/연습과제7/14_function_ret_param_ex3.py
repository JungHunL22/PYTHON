def order(price,qty) :

    amount=price*qty

    if amount>=100000:
        discount=int(0.1*amount)
    elif amount>=50000 and amount<100000:
        discount=int(0.05*amount)
    else:
        discount=int(0*amount)
    total=amount-discount
    print("------------------------")
    print("주문액 : %s원" %amount)
    print("할인액 : %s원" %discount)
    print("지불액 : %s원" %total)

p=int(input("상품 가격 입력 : "))
q=int(input("주문 수량 입력 : "))
order(p,q)
