f=open('test2.txt','r',encoding='utf-8')
data=f.read()
print(data)
print(type(data))
for i in data:
    print(i)
f.close()
