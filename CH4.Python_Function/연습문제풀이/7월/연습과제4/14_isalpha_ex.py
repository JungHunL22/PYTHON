sentence=input("문장을 입력하세요 : ")
roop=len(sentence)
alpha,digit,space,etc=0,0,0,0
for i in range(roop):
    if sentence[i].isalpha()==True:
        alpha+=1
    elif sentence[i].isdigit()==True:
        digit+=1
    elif sentence[i].isspace()==True:
        space+=1
    else :
        etc+=1
print("알파벳 : %d개"%alpha)
print("숫자 : %d개"%digit)
print("스페이스 : %d개"%space)
print("기타 : %d개"%etc)

#나의 email 주소는 python777@naver.com 입니다!