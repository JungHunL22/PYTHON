print('----------------메뉴판----------------')
f = open('메뉴판.txt', 'r', encoding='utf-8')
file = list()
# 해당파일의 총 라인수를 알 수 없으므로 무한반복 루프
while True:
    line = f.readline()
    if not line:  # 라인에 읽은내용이 없으면
        break
    file.append(line)
    # end=''로 print문 자체의 줄바꿈은 하지 않음
    # (원본에 엔터키를 쳤으므로)
f.close()
key = list()
value = list()
for i in range(len(file)):
    file[i] = file[i].replace("\n", "").split(':')
    for j in range(len(file[i])):
        if j == 0:
            key.append(file[i][j])
        elif j == 1:
            value.append(file[i][j])
menu=dict(zip(key,value))
product=input('무엇을 주문하시겠습니까')
if product in menu.keys() :
    print("있음")
else:
    print("없음")