#13_키워드위치인수
def student_info(name,age,gender):
    student={
        'name':name,
        'age':age,
        'gender':gender
    } #자료를 입력받아 딕셔너리로 구성 후 반환하는 함수
    return student
#호출테스트 (위치인수,키워드인수)
print(student_info(name='kim',age='23',gender='여')) #키워드인수
print(student_info('lee',25,'남')) #위치인수
print(student_info('hong',gender='여',age='22'))

#키워드가 위치앞에 나오면 에러
print(student_info(gender='여'),'park',28)
print(student_info('lee',age=25,'남'))

#남 두번째 인수기 때문에 매개변수 age에 대입되고 age=25인수에 의해 age에 대입
print(student_info('lee','남',age=25))
