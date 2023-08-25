from abc import abstractmethod, ABCMeta

class Payment(metaclass=ABCMeta): #subejct
    @abstractmethod
    def do_pay(self):
        pass
    
class Bank(Payment): #realSubject, client가 필요한 기능들은 모두 여기에서 구현
    
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
        #금액이 충분한지 체크
        print("Bank:: Checking if Acoount", self.__getAccount(), "has enough funds")
        return False
        
    def do_pay(self): 
        if self.__hasFunds():
            print("Bank::Paying the merchant")
            return True
        else:
            print("Bank:Sorry, not enough funds!")
            return False
    
class DebitCard(Payment): #proxy
    def __init__(self):
        self.bank = Bank() #realSubject 객체 생성
    
    def do_pay(self): #realSubject 클래스의 메서드 호출 정도만 가능함
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.setCard(card)
        return self.bank.do_pay() #같이 상속받은 메서드를 호출했음
    
class You: #client
    def __init__(self):
        print("You:: Lets buy the Denim shirt")
        self.debitCard = DebitCard() #proxy 객체 생성
        self.isPurchased = None
        
    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()
            
you = You()
you.make_payment()