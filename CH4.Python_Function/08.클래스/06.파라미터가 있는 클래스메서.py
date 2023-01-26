class Rectangle :
    # 객체 변수를 생성할 때 한번 호출됨
    def __init__(self,width=1,height=1):
        print('self : ',self)
        self.width=width
        self.height=height

    # instance 메서드 - 객체(인스턴스를 이용해서 호출)
    def calcArea(self,width,height):
        if width > 0 and height > 0:
            area=width*height
        else :
           area = self.width * self.height
        return area

r_1=Rectangle()
#width와 height가 0을 넘지못하면 초기값으로 면적계산
print("r_1의 면적 :", r_1.calcArea(0,0))
#width와 height가 0을 넘으면 변수값으로 면적계산
print("r_1의 면적 :", r_1.calcArea(5,3))