#스태틱 메서드/클래스 메서드 두 가지 사용

class Math :
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def multiply(a,b):
        return a*b


#클래스 메서드로 사용
print("클래스메서드로 접근 : ",Math.add(10,20))
print("클래스메서드로 접근 : ",Math.multiply(10,20))

# 일반 객체 메서드로 접근
m_o=Math() #객체 인스턴스 생성 방식으로도 사용가능
print("객체메서드로 접근 : ",m_o.add(10,20))
print("객체메서드로 접근 : ",m_o.multiply(1,20))