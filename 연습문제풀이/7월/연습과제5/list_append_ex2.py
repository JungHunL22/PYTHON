grade=list()
sum=0
avg=0
for i in range(1,6):
    student=int(input("학생%d 점수 입력 : "%i))
    grade.append(student)
    sum+=grade[i-1]
    avg=sum/i
print(grade)
print("총점 : %d"%sum)
print("평균 : %.2f"%avg)