def get_area():
    width=int(input("가로길이입력 : "))
    height = int(input("세로길이입력 : "))
    area =width*height
    return area

rect_area = get_area()
print("사각형의 면적 : %d" %rect_area) #함수 호출 후반환된 결과 값이 호출한 코드 자리로 전달