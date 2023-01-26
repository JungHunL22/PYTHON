student=[{"name": "홍길동", "korean": 87, "math": 98, "english": 88, "science":95},
         {"name": "이몽룡", "korean": 92, "math": 98, "english": 96, "science": 98},
         {"name": "성춘향", "korean": 76, "math": 96, "english": 94, "science": 90},
         {"name": "변학도", "korean": 98, "math": 92, "english": 96, "science": 92},
         {"name": "박지성", "korean": 95, "math": 98, "english": 98, "science": 98},
         {"name": "류현진", "korean": 64, "math": 88, "english": 92, "science": 92},
]
sum=list()
avg=list()
print("이름 \t총점 \t평균")
for i in range(len(student)):
    sum.append(0)
    avg.append(0)
    grade=list(student[i].values())
    score=grade[1:5]
    for j in range(len(score)):
        sum[i]+=score[j]
        avg[i]=sum[i]/len(score)
    print("%s \t%d \t%.2f"%(grade[0],sum[i],avg[i]))
# print(sum)
# print(avg)



