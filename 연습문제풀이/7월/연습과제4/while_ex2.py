i=int(input("마지막 숫자를 입력하세요: "))
num=1
sum=0
while num<=i:
    if num%2==1:
        sum+=num
    num+=1
print("1부터 %d까지의 홀수의 합은 %d 입니다."%(i,sum))
#1 3 5 7 9