class Calc_s:
    num=10
    @staticmethod
    def calc(x):
        # return x+10
        # staticmethod 메서드인 경우에 클래스 속성을 사용하기 위해서는 클래스명을 이용
        return x+Calc_s.num+10
# 클래스 외부에서 전달되는 인수만 사용하는 메서드인 경우는 @staticmethod를 사용하나
# @classmethod를 사용하나 동일한 기능을 하게 된다.


class Calc_c:
    num=10
    @classmethod
    def calc(cls,x):
        #return x+10
        return x+cls.num+10
        # cls가 self기능을 함
        # @classmethod 메서드인 경우에 클래스 속성을 사용하기 위해서는
        # 첫번쨰 파라미터(cls)를 이용한다다print(Calc_s.calc(10))

print(Calc_c.calc(20))
print(Calc_s.calc(20))