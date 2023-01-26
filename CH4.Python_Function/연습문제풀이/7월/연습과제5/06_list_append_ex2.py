grade=list()
sum=0
avg=0
n=0
num=int(input("학생 수 입력 : "))
for i in range(1,num+1):
    student=int(input("학생%d 점수 입력 : "%i))
    grade.append(student)
    sum += grade[i - 1]
    avg=sum/i
    if grade[i-1]>=80:
        n+=1

print(grade)
print("총점 : %d"%sum)
print("평균 : %.2f"%avg)
print("80 이상 학생 : %d명"%n)