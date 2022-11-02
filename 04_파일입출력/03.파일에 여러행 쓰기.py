#여러행으로 표시될 문자열을 생성해서 문자열 하나를 쓴다
f=open("file3.txt",'w',encoding='UTF-8')
#for i in range(1,11):
#    data='%d행\n'%i
#    f.write(data)
data=''
for i in range(1,11):
    data=data+'%d행\n'%i

f.write(data)
f.close()