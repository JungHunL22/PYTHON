# 1. 숫자하나를 증가시키는 기능 : increment()
# 2. 숫자를 0으로 초기화 하는 기능 : reset()
# 3. 현재 count된 숫자를 출력하는 기능 : print_current_value()

# 특성(속성,변수)
# 카운팅 결과를 저장하는 변수 : cnt

class count:
    def __init__(self):
        self.cnt = 0
    # 클래스 메서드 1
    def increment(self):
        self.cnt+=1
    # 클래스 메서드 2
    def reset(self):
        self.cnt = 0
    def print_current_value(self):
        print("현재 카운트된 값은 : ",self.cnt)

a=count()
b=count()

a.increment(); a.increment()
b.increment(); b.increment()
a.increment()
#결과 값 3,2
a.print_current_value()
b.print_current_value()

b.increment()
b.reset()
b.increment()

a.print_current_value()
b.print_current_value()