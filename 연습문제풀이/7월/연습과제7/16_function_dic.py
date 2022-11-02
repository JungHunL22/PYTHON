def show_info(name,year,age,phone):
    info={'name':name,'year':int(year),'age':int(age),'phone':phone}
    return info
var1=input("이름 : ")
var2=input("학년 : ")
var3=input("나이 : ")
var4=input("연락처 : ")
people=show_info(var1,var2,var3,var4)
print(people)