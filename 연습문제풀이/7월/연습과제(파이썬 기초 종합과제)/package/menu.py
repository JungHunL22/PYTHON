# 메뉴판 불러오기,딕셔너리로 만들기
def menu():
    f=open('package/메뉴판.txt', 'r', encoding='utf-8')
    file=list()
    while True:
        line=f.readline()
        if not line:
            break
        file.append(line)
    f.close()
    key=list()
    value=list()
    for i in range(len(file)):
        file[i]=file[i].replace("\n","").split(':')
        for j in range(len(file[i])):
            if j==0:
                key.append(file[i][j])
            elif j==1:
                value.append(file[i][j])
    food=dict(zip(key,value))
    print('----------------메뉴판----------------')
    for i,j in zip(key,value):
        print('{:>15}\t'.format(i)+'{} 원'.format(j))
    print('------------------------------------')
    return food

