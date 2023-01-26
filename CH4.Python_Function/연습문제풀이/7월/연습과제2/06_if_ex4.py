n1=int(input("정수 1 입력 : "))
n2=int(input("정수 2 입력 : "))
n3=int(input("정수 3 입력 : "))
if n1>n2 and n1>n3:
    print("제일 큰 수 : %d"%n1)
elif n2>n1 and n2>n3:
    print("제일 큰 수 : %d"%n2)
else:
    print("제일 큰 수 : %d"%n3)

