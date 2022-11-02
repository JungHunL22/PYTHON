print("-----------파일 내에서 검색 : seek()------------")
f=open("test2.txt",'r',encoding='utf-8')
f.seek(0,0) #열,행 0열 0행부터 시작
lines=f.readlines()
print(lines)
#결과값 ['01234\n', 'abcde\n', '가나다라마']

print("-----------파일 내에서 검색 : seek()------------")
f.seek(1,0) #열,행 1열 0행부터 시작
lines=f.readlines()
print(lines)
#결과값 ['1234\n', 'abcde\n', '가나다라마']

print("-----------파일 내에서 검색 : seek()------------")
#7열은 a
f.seek(7,0) #열,행 7열 0행부터 시작
lines=f.readlines()
print(lines)
#결과값 ['abcde\n', '가나다라마']

print("-----------파일 내에서 검색 : seek()------------")
#한글은 보통은 2바이트 사용
#utf-8은 초성중성종성을 나눠 3바이트를 사용
#가=14,15,16차지/나=17,18,19차지
f.seek(20,0) #열,행 7열 0행부터 시작
lines=f.readlines()
print(lines)
f.close()