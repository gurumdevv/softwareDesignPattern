#주문 유효성 검사 -> 할인 적용 -> 결제 처리
#주문: 주문 번호, 주문 금액
#주문 유효성 검사: 주문 금액이 0보다 커야 유효한 주문으로 간주됨
#할인 적용: 주문 금액에 할인율을 적용, 할인율은 하위 클래스에서 설정
#결제 처리 단계: 주문금액이 실제로 결제되는 것으로 가정, 주문 번호와 최종 결제 금액을 출력
from abc import abstractmethod, ABCMeta

class OrderProcessor(metaclass=ABCMeta):    #알고리즘 요소 정의(abstractMethod), 알고리즘 순서 정의(templateMethod)  
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def validateOrder(self):    #주문 유효성 검사
        pass
    
    @abstractmethod
    def applyDiscount(self):    #할인 적용
        pass
    
    @abstractmethod
    def processPayment(self):   #결제 처리
        pass

    def processOrder(self):
        self.check = self.validateOrder()
        if self.check == True:
            self.applyDiscount()
            self.processPayment()
        else:
            print("주문 금액을 확인해주세요.")
        
class DiscountedOrderProcessor(OrderProcessor):     #abstractMethod 구현
    def __init__(self, orderNum, orderPrice):
        self.orderNum = orderNum
        self.orderPrice = orderPrice
        self.discount = 0.9
        self.totalPrice = 0
        
    def validateOrder(self):
        if self.orderPrice > 0:
            return True
        else:
            return False
        
    def applyDiscount(self):    #할인율 10%
        self.totalPrice = self.orderPrice * self.discount
        
    def processPayment(self):        
        print("할인률: 10%")
        print("할인 적용 후 금액:", self.totalPrice)
        print("결제 처리 완료")
        print("주문 번호:", self.orderNum)
        print("주문 금액:", self.orderPrice)

class DoOrder:      #concreteClass 인스턴스 생성 class
    def __init__(self, orderNum, orderPrice):
        self.orderNum = orderNum
        self.orderPrice = orderPrice
        
    def main(self):
        self.order = DiscountedOrderProcessor(self.orderNum, self.orderPrice)
        self.order.processOrder()
    
doOrder = DoOrder(1020, 2000)
doOrder.main()