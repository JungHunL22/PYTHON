#파일을 쓰기모드로 연다
#해당 파일이 존재하면 덮어씀
#해당파일이 존재하지 않으면 새로 생성

#파일생성 : 파일명만 적으면 현재 디렉터리에 생성
#변수 지정하지않으면 close불가하므로 변수f에 지정
#실행후 반환되는 파일 포인터를 반드시 저장
#f=open('file.txt','w')
#파일닫기
#f.close()

#파일생성 (특정디렉터리에 생성)
#FileNotFoundError: [Errno 2] No such file or directory: 'c:/python/file1.txt'
#없는 폴더라서 에러
#f=open('c:/python/file1.txt','w')
#현재디렉터리 밑에 res디렉터리가 있어야 함
#현재디렉터리에서 찾아라 ./res
f=open('./res/file1.txt','w')
f.close()

# 파일경로
# 상대경로 : 현재 디렉터리를 기준으로 경로 생성
# res/f.txt : 현재 디렉터리 밑에서 res디렉터리 찾고 그 안에 f.txt
# ./res/f.txt : 현재 디렉터리 밑에서 res디렉터리 찾고 그 안에 f.txt
# ../res/f.txt : 현재 디렉터리보다 한 레벨 위 디렉터리에서 res디렉터리 찾고 그 안에 f.txt
g=open('../res/f.txt','w')
g.close()

# 절대경로
# 드라이브부터 나열하는 경로
# c:/mydoc/file1.txt