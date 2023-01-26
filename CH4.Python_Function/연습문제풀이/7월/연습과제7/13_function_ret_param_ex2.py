def get_interest(amount,rate):
    interest=int(amount*(rate*0.01))
    return interest

deposit=eval(input("예금액 입력 : "))
int_rate=eval(input("이자액 입력(%) : "))
int1=get_interest(deposit,int_rate)
print("이자액 : "+format(int1,',')+"원")