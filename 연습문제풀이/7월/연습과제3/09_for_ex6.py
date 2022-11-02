positive=0
negative=0
zero=0
for i in range(1,11):
    num=int((input("숫자%d입력 : "%i)))
    if num>0 :
        positive+=1

    elif num<0:
        negative+=1

    else:
        zero+=1
print("----------------------------")
print("양의 개수 : %d"%positive)
print("음의 개수 : %d"%negative)
print("0의 개수 : %d"%zero)
