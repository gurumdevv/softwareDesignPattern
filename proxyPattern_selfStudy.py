#realSubject의 do_pay()와 proxy의 do_pay()를 어떻게 구현했는지 유심히 보자!
from abc import abstractmethod, ABCMeta

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None
        
    def setCard(self, card):
        #카드 정보를 은행에 전달
        self.card = card
        
    def __getAccount(self):
        #카드 소지자의 계좌 정보를 조회, 카드 번호와 계좌 번호가 같도록 구현
        self.account = self.card
        return self.account
    
    def __hasFunds(self):
        #해당 계좌에 셔츠를 구입하기에 충분한 돈이 있는지 확인
        print("계좌<", self.__getAccount(), ">에 현재 잔액이 충분한지 확인중...")
        return True
        
    def do_pay(self):
        if self.__hasFunds():
            print("결제에 성공했습니다!")
        else:
            print("현재 잔액이 부족합니다")
    
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()
        
    def do_pay(self, card):
        self.bank.setCard(card)
        return self.bank.do_pay()
            
class You:
    def __init__(self):
        self.payment = DebitCard()
        
    def make_payment(self):
        print("청바지 결제를 시도합니다...")
        self.card = input("카드 번호를 입력해주세요: ")
        self.payment.do_pay(self.card)
        
you = You()
you.make_payment()
        
    