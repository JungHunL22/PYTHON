# # 에러 종류와 상관없이 에러가 발생하면 except수행
# # 어떤 에러가 발생했는지 파악하기 위해서 에러메세지를 받아야함
# try :
#     #print(10/0)
#     print("나이"+23)
#
# except :
#     print("오류발생")
# #최상위 에러인 exception 적어도됨
# try:
#     # print(10/0)
#     print("나이" + 23)
#
# except Exception:
#     print("오류발생")
#
# try:
#     print(10/0)
#     #print("나이" + 23)
#
# except ZeroDivisionError:
#     print("오류발생")
#
# # 오류가 발생하는 순간 except로 넘어가서 처리, 예외처리하고 문장 종료(위로 다시 돌아오지 않음)
# try:
#     print(10/0) #zero division error
#     print("나이" + 23) #type error
#
# except ZeroDivisionError:
#     print("오류발생")
# # 오류가 발생하는 순간 except로 넘어가서 처리하지만 type에러에 except문에 예외처리 안돼 있어 오류
# try:
#     print("나이" + 23) #type error
#     print(10/0) #zero division error
#
# except ZeroDivisionError:
#     print("오류발생")

# 예외 종류 명시
# 숫자를 입력하지 않은 경우 valueError
# 정수형 숫자만 입력받아야 되는 경우

# 정수를 입력받지 않은 경우에 대해서만 예외처리
# try :
#     num = int(input("정수를 입력하세요. "))
# except ValueError :
#     print("정수가 아닙니다.")
# else:
#     print(num + 10)
# finally:
#     print("프로그램을 종료합니다.")

# 에러 종류 명시 메시지 변수 사용 가능
try :
    print(10/0) # ZeroDivisionError
except ZeroDivisionError as e: #에러에 해당하는 메시지를 e에 할당한다는 문장
    print("0으로 나눌 수 없습니다.",e)
#zero~에러를 예외처리 했으므로 실행을 멈추지 않고 다음 문장도 처리 가능
print(3+5)

#여러 개의 예외처리문이 있으면
# a=[1,2,3]
# try :
#     print(10/0) # 첫번쨰 오류 예외처리 실행
#     print(a[4]) # 처리되지 않음
# except ZeroDivisionError as e:
#     print("0으로 나눌 수 없습니다.",e)
# except IndexError as e:
#     print("인덱스 범위를 벗어 났습니다.",e)
#
# # 첫 문장이 오류가 아닐 때
# try :
#     print(10/2)
#     print(a[4])
#     # 첫번쨰 문장이 에러가 아니므로 1번 예외처리는 넘어가고 2번 예외처리 실행
# except ZeroDivisionError as e:
#     print("0으로 나눌 수 없습니다.",e)
# except IndexError as e:
#     print("인덱스 범위를 벗어 났습니다.",e)
#
# #여러 개의 예외를 한번에 처리
# try :
#     print(10/0)
#     print(a[4])
#
# except (ZeroDivisionError, IndexError) as e: #예외처리 or도 가능
#     print("오류가 발생 헀습니다.",e)

try :
    f=open("exception.txt",'r')
except FileNotFoundError:
    pass
else :
    data = f.read()
    print(data)
    f.close()
print("종료")


try :
    f=open("exception.txt",'r')
except FileNotFoundError:
    pass
else :
    data = f.read()
    print(data)
    f.close()
finally:
    print("종료")