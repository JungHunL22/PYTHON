#13_function_ret_param_ex2.py
#get_interest()
#예금액과 이자율을 전달 받아서 이자액을 구하여 반환
#deposit , int_rete , interest 변수명

def get_interest(dps,rate) : #예금액과 이자율 전달받음(매개변수)
    inter=dps*rate/100
    return int(inter)
    return int(dps*rate/100)

deposit=int(input("예금액 입력 :"))
int_rate=float(input("이자율 입력(%) :"))
interest=format(get_interest(deposit,int_rate), ",")
#format함수로 1000단위 구분자를 넣으면 문자열로 인식함
print("이자액 : %s원" %interest)