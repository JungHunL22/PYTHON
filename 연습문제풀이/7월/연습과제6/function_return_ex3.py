def order():
    price=int(input("상품가격 입력 : "))
    quan=int(input("주문수량 입력 : "))
    total=price*quan
    print("-------------------------")
    print("상품가격 : %d원"%price)
    print("주문수량 : %d개"%quan)
    print("주문액 : %d원"%total)
order()