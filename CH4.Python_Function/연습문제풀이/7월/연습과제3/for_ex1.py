a=int(input("숫자 1 입력 : "))
b=int(input("숫자 2 입력 : "))
sum=0
for i in range(a,b+1):
    sum+=i
print("%d부터 %d까지의 합: "%(a,b),sum)