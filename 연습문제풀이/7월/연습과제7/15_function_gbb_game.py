from random import randint
def gbb_game(me):
    com=randint(1,3)
    if  me-com==1 or (me==1 and com==3):
        print("당신이 이겼습니다.")

    elif com-me==1 or (me==3 and com==1):
       print("컴퓨터가 이겼습니다.")
    else:
        print("비겼습니다.")


    print("com : %d"%com)
ex=int(input("YOU 입력 : 1:가위 2:바위 3:보 : "))
gbb_game(ex)

#내가 이기는 경우 21 32 13
#컴이 이기는 경우 12 23 31