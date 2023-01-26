# #try ... except문 사용
# try :
#     예외발생가능한 문장1
# except 예외유형 :
#     예외처리문장2
# else :
#     예외 없을 떄 수행 문장3
# finally :
#     예외 유무와 상관없이 실행되는 문장4
#
# else ~ finally는 생략가능
# 1번문장을 실행 - 오류발생(예외처리 되어 있는 오류면) 2번문장 수행 - 4번문장을 수행
# 1번문장을 실행 - 오류없으면 3번문장 수행 - 4번문장을 수행

# 에러확인
# ZeroDivisionError: division by zero
# print(10/0)

# TypeError: can only concatenate str (not "int") to str
# print("나이 : "+ 23 + "살")

# NameError: name 'b' is not defined
# print(b)

# ValueError: incomplete format
# c=100
# print("%d%"%c) %는 %%로 출력가능

# # SyntaxError: expected ':'
# x=100
# if x>10
#     print('홍길동')

# IndexError: list index out of range
# a=[1,2,3,4]
# print(a[4])

# UnboundLocalError: local variable 'a' referenced before assignment
# def add():
#     a=a+1

# add()

# ModuleNotFoundError: No module named 'mymodule'
# import mymodule

# FileNotFoundError: [Errno 2] No such file or directory: 'e.txt'
# f=open('e.txt','r')
# data=f.read()
# print(data)

# OSError: [Errno 22] Invalid argument: 'd:\x0cile\\exceptinon.txt'
# f=open("d:\file\exceptinon.txt",'w')
# 경로 지정 시 \\ 사용 or / 사용