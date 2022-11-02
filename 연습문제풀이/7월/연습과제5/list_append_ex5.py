product=list()
while True:
    goods = input('상품 등록 (엔터키 누르면 종료) : ')
    product.append(goods)
    if goods=='':
        break
print("등록된 상품 :",end=' ')
for i in range(len(product)):
    print("%s"%product[i],end=' ')