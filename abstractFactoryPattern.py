from abc import abstractmethod, ABCMeta

class PizzaFactory(metaclass=ABCMeta): #AbstractFactory 인터페이스
    
    @abstractmethod
    def createVegPizza(self): #ConcreteFactory 인스턴스 생성 추상메서드
        pass
    
    @abstractmethod
    def createNonVegPizza(self): #ConcreteFactory 인스턴스 생성 추상메서드
        pass
    
    
    
class IndianPizzaFactory(PizzaFactory): #ConcreteFactory1
    
    def createVegPizza(self):
        return DeluxVeggiePizza() #ConcreteProduct1 인스턴스 생성
    def createNonVegPizza(self):
        return ChickenPizza() #AnotherConcreteProduct1 인스턴스 생성
    
class USPizzaFactory(PizzaFactory): #ConcreteFactory2
    
    def createVegPizza(self):
        return MexicanVegPizza() #ConcreteProduct2 인스턴스 생성
    def createNonVegPizza(self):
        return HamPizza() #AnotherConcreteProduct2 인스턴스 생성
        
        
        
class VegPizza(metaclass=ABCMeta): #AbstractProduct 인터페이스
    
    @abstractmethod
    def prepare(self, VegPizza): #ConcreteProduct 인스턴스 생성 추상 메서드
        pass
    
class NonVegPizza(metaclass=ABCMeta): #AnotherAbstractProdcut 인터페이스
    
    @abstractmethod
    def serve(self, VegPizza): #AnotherConcreteProduct 인스턴스 생성 추상 메서드
        pass
    
    
    
class DeluxVeggiePizza(VegPizza): #ConcreteProduct1 구현
    
    def prepare(self):
        print("Prepare ", type(self).__name__)
        
class ChickenPizza(NonVegPizza): #AnotherConcreteProduct1 구현
    
    def serve(self, VegPizza):
        print(type(self).__name__, "is served with Chicken on", type(VegPizza).__name__)
        
class MexicanVegPizza(VegPizza): #ConcreteProduct2 구현
    
    def prepare(self):
        print("Prepare ", type(self).__name__)

class HamPizza(NonVegPizza): #AnotherConcreteProduct2 구현
    
    def serve(self, VegPizza):
        print(type(self).__name__, "is served with Ham on", type(VegPizza).__name__)

class PizzaStore:
    
    def __init__(self):
        pass
    
    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)
            
pizza = PizzaStore()
pizza.makePizzas()